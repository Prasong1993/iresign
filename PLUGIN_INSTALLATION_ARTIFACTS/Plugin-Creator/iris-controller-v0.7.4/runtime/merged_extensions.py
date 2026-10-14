"""Additive SQLite-backed usage ledger and deterministic project policy for IRIS."""
import json, uuid
from datetime import datetime, timezone
import database

ALLOWED_PHASES = {"MCR", "SRR", "PDR", "CDR", "TRR", "ORR"}


def now():
    return datetime.now(timezone.utc).isoformat()


def init_extensions():
    database.init_db()
    with database.get_connection() as c:
        c.executescript("""
        CREATE TABLE IF NOT EXISTS usage_records (
          usage_id TEXT PRIMARY KEY, category TEXT NOT NULL, action TEXT NOT NULL,
          value_json TEXT NOT NULL, unit TEXT, source TEXT, status TEXT NOT NULL DEFAULT 'RECORDED',
          notes TEXT, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS usage_audit (
          id INTEGER PRIMARY KEY AUTOINCREMENT, usage_id TEXT NOT NULL, event TEXT NOT NULL,
          fields_json TEXT NOT NULL DEFAULT '[]', occurred_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS project_controls (
          project_id TEXT PRIMARY KEY, budget_limit REAL, budget_used REAL NOT NULL DEFAULT 0,
          current_phase TEXT NOT NULL DEFAULT 'MCR', allowed_phases_json TEXT NOT NULL,
          updated_at TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_usage_category_status ON usage_records(category,status);
        CREATE INDEX IF NOT EXISTS idx_usage_audit_id ON usage_audit(usage_id,id);
        """)
        c.execute("INSERT OR IGNORE INTO schema_migrations(version,name) VALUES(2,'merged_usage_and_project_policy')")


def _row(row):
    if row is None: return None
    d = dict(row)
    d['value'] = json.loads(d.pop('value_json'))
    return d


def usage_record(a):
    category, action = a.get('category'), a.get('action')
    if not isinstance(category, str) or not category.strip(): raise ValueError('USAGE_CATEGORY_REQUIRED')
    if not isinstance(action, str) or not action.strip(): raise ValueError('USAGE_ACTION_REQUIRED')
    if 'value' not in a or a.get('value') is None: raise ValueError('USAGE_VALUE_REQUIRED')
    uid, ts = str(uuid.uuid4()), now()
    with database.get_connection() as c:
        c.execute("INSERT INTO usage_records(usage_id,category,action,value_json,unit,source,status,notes,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?)",
          (uid,category.strip(),action.strip(),json.dumps(a['value'],ensure_ascii=False,sort_keys=True),a.get('unit'),a.get('source'),a.get('status','RECORDED'),a.get('notes'),ts,ts))
        c.execute("INSERT INTO usage_audit(usage_id,event,fields_json,occurred_at) VALUES(?,?,?,?)",(uid,'CREATED','[]',ts))
    return usage_get({'usage_id':uid})


def usage_list(a):
    sql, params = "SELECT * FROM usage_records WHERE 1=1", []
    if a.get('category') is not None: sql += " AND category=?"; params.append(a['category'])
    if a.get('status') is not None: sql += " AND status=?"; params.append(a['status'])
    sql += " ORDER BY created_at DESC"
    rows = database.many(sql, params)
    return {'count':len(rows),'records':[_row(r) for r in rows]}


def usage_get(a):
    uid = a.get('usage_id')
    row = database.one("SELECT * FROM usage_records WHERE usage_id=?",(uid,))
    if not row: raise ValueError('USAGE_RECORD_NOT_FOUND')
    d = _row(row)
    d['audit'] = database.many("SELECT event,fields_json,occurred_at FROM usage_audit WHERE usage_id=? ORDER BY id",(uid,))
    for item in d['audit']: item['fields'] = json.loads(item.pop('fields_json'))
    return d


def usage_update(a):
    uid, updates = a.get('usage_id'), a.get('updates')
    if not isinstance(updates,dict) or not updates: raise ValueError('USAGE_UPDATES_REQUIRED')
    allowed={'category','action','value','unit','source','status','notes'}
    unknown=set(updates)-allowed
    if unknown: raise ValueError('INVALID_USAGE_FIELDS:'+','.join(sorted(unknown)))
    if 'category' in updates and (not isinstance(updates['category'],str) or not updates['category'].strip()): raise ValueError('USAGE_CATEGORY_REQUIRED')
    if 'action' in updates and (not isinstance(updates['action'],str) or not updates['action'].strip()): raise ValueError('USAGE_ACTION_REQUIRED')
    if 'value' in updates and updates['value'] is None: raise ValueError('USAGE_VALUE_REQUIRED')
    if not database.one("SELECT usage_id FROM usage_records WHERE usage_id=?",(uid,)): raise ValueError('USAGE_RECORD_NOT_FOUND')
    mapping={'category':'category','action':'action','value':'value_json','unit':'unit','source':'source','status':'status','notes':'notes'}
    sets, vals = [], []
    for key,val in updates.items():
        sets.append(mapping[key]+'=?')
        vals.append(json.dumps(val,ensure_ascii=False,sort_keys=True) if key=='value' else (val.strip() if key in ('category','action') and isinstance(val,str) else val))
    ts=now(); sets.append('updated_at=?'); vals.extend([ts,uid])
    with database.get_connection() as c:
        c.execute('UPDATE usage_records SET '+','.join(sets)+' WHERE usage_id=?',vals)
        c.execute("INSERT INTO usage_audit(usage_id,event,fields_json,occurred_at) VALUES(?,?,?,?)",(uid,'UPDATED',json.dumps(sorted(updates)),ts))
    return usage_get({'usage_id':uid})


def create_project(a):
    name = str(a.get('name','')).strip()
    if not name: raise ValueError('PROJECT_NAME_REQUIRED')
    pid = str(a.get('project_id') or uuid.uuid4())
    budget = a.get('budget_limit')
    if budget is not None and float(budget)<0: raise ValueError('BUDGET_MUST_BE_NONNEGATIVE')
    phases = a.get('allowed_phases') or sorted(ALLOWED_PHASES)
    if not isinstance(phases,list) or not phases or any(p not in ALLOWED_PHASES for p in phases): raise ValueError('INVALID_PHASE_POLICY')
    phase = a.get('current_phase','MCR')
    if phase not in phases: raise ValueError('CURRENT_PHASE_NOT_ALLOWED')
    with database.get_connection() as c:
        c.execute("INSERT INTO projects(project_id,name,status,config_json) VALUES(?,?,?,?)",(pid,name,'ACTIVE',json.dumps({'source':'merged-controller'},ensure_ascii=False)))
        c.execute("INSERT INTO project_controls(project_id,budget_limit,budget_used,current_phase,allowed_phases_json,updated_at) VALUES(?,?,?,?,?,?)",(pid,budget,0,phase,json.dumps(phases),now()))
        c.execute("INSERT INTO audit_log(work_id,action,details) VALUES(?,?,?)",(pid,'PROJECT_CREATED',json.dumps({'name':name,'budget_limit':budget,'current_phase':phase})))
    database.record_event('PROJECT_CREATED',status='ACTIVE',payload={'project_id':pid,'name':name})
    return {'project_id':pid,'name':name,'status':'ACTIVE','budget_limit':budget,'budget_used':0,'current_phase':phase,'allowed_phases':phases}


def check_project_policy(a):
    pid=str(a.get('project_id','')).strip()
    project=database.one("SELECT * FROM projects WHERE project_id=?",(pid,))
    controls=database.one("SELECT * FROM project_controls WHERE project_id=?",(pid,))
    if not project or not controls: return {'passed':False,'project_id':pid,'errors':['PROJECT_NOT_FOUND']}
    errors=[]
    if project['status'] not in ('ACTIVE','IN_PROGRESS'): errors.append('PROJECT_NOT_ACTIVE')
    phase=a.get('phase') or controls['current_phase']
    phases=json.loads(controls['allowed_phases_json'])
    if phase not in phases: errors.append('PHASE_NOT_ALLOWED')
    amount=float(a.get('budget_amount',0) or 0)
    if amount<0: errors.append('BUDGET_AMOUNT_NEGATIVE')
    if controls['budget_limit'] is not None and float(controls['budget_used'])+amount>float(controls['budget_limit']): errors.append('BUDGET_EXCEEDED')
    title=a.get('title')
    if title:
        dup=database.one("SELECT task_id FROM tasks WHERE project_id=? AND title=? AND status IN ('PENDING','QUEUED','RUNNING','COMPLETED')",(pid,title))
        if dup and not a.get('allow_rerun',False): errors.append('DUPLICATE_TASK')
    return {'passed':not errors,'project_id':pid,'phase':phase,'budget_limit':controls['budget_limit'],'budget_used':controls['budget_used'],'budget_requested':amount,'errors':errors}


def create_controlled_task(a, base):
    check=check_project_policy(a)
    if not check['passed']: raise ValueError('POLICY_DENIED:'+','.join(check['errors']))
    title=str(a.get('title','')).strip()
    if not title: raise ValueError('TASK_TITLE_REQUIRED')
    wid=str(a.get('work_id') or uuid.uuid4())
    tid=str(a.get('task_id') or uuid.uuid4())
    base.create_work(wid,title)
    amount=float(a.get('budget_amount',0) or 0)
    ts=now()
    with database.get_connection() as c:
        c.execute("INSERT INTO tasks(task_id,project_id,work_id,title,status,assignee,started_at,input_json) VALUES(?,?,?,?,?,?,?,?)",(tid,a['project_id'],wid,title,'PENDING',a.get('assignee'),ts,json.dumps({'phase':check['phase'],'budget_amount':amount},ensure_ascii=False)))
        c.execute("UPDATE project_controls SET budget_used=budget_used+?,current_phase=?,updated_at=? WHERE project_id=?",(amount,check['phase'],ts,a['project_id']))
        c.execute("INSERT INTO audit_log(work_id,action,details) VALUES(?,?,?)",(wid,'POLICY_ALLOWED',json.dumps(check,ensure_ascii=False)))
    database.record_event('CONTROLLED_TASK_CREATED',work_id=wid,task_id=tid,status='PENDING',payload={'project_id':a['project_id'],'title':title,'policy':check})
    return {'task_id':tid,'work_id':wid,'title':title,'status':'PENDING','policy':check}
