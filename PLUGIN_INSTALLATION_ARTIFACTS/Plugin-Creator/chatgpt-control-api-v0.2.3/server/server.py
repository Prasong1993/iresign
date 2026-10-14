#!/usr/bin/env python3
import json, os, sys, uuid, datetime

ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
STATE_DIR=os.path.join(ROOT,'.state')
os.makedirs(STATE_DIR, exist_ok=True)
STATE_FILE=os.path.join(STATE_DIR,'tasks.json')
USAGE_FILE=os.path.join(STATE_DIR,'usage.json')
ALLOWED_EVIDENCE={'OFFICIAL','VERIFIED','CROSS_VERIFIED'}
STEPS={1:'RECEIVE',2:'ANALYZE_RESEARCH',3:'VALIDATE',4:'EXECUTE',5:'VERIFY'}
TERMINAL={'COMPLETED'}

def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def load_file(path):
    try:
        with open(path,'r',encoding='utf-8') as f: return json.load(f)
    except FileNotFoundError: return {}
def save_file(path,x):
    tmp=path+'.tmp'
    with open(tmp,'w',encoding='utf-8') as f: json.dump(x,f,ensure_ascii=False,indent=2)
    os.replace(tmp,path)
def load(): return load_file(STATE_FILE)
def save(x): save_file(STATE_FILE,x)
def load_usage(): return load_file(USAGE_FILE)
def save_usage(x): save_file(USAGE_FILE,x)
def new_attempt(task, original_input):
    aid=str(uuid.uuid4())
    task['attempt_id']=aid; task['status']='RECEIVED'; task['current_step']=1
    task['input']=original_input; task['evidence']=[]; task['findings']=[]; task['plan']=[]; task['execution']=[]; task['verification']=[]; task['route']={}; task['errors']=[]
    task['audit'].append({'at':now(),'event':'ATTEMPT_CREATED','attempt_id':aid,'step':1})
def err(msg): raise ValueError(msg)
def get_task(tasks, tid):
    if tid not in tasks: err('TASK_NOT_FOUND')
    return tasks[tid]
def require_step(t, step):
    if t['current_step']!=step: err(f'INVALID_STEP_EXPECTED_{t["current_step"]}_GOT_{step}')
def usage_handle(name,a):
    records=load_usage()
    if name=='record_usage':
        category=a.get('category'); action=a.get('action'); value=a.get('value')
        if not isinstance(category,str) or not category.strip(): err('USAGE_CATEGORY_REQUIRED')
        if not isinstance(action,str) or not action.strip(): err('USAGE_ACTION_REQUIRED')
        if value is None: err('USAGE_VALUE_REQUIRED')
        record_id=str(uuid.uuid4()); ts=now()
        record={'usage_id':record_id,'created_at':ts,'updated_at':ts,'category':category.strip(),'action':action.strip(),'value':value,'unit':a.get('unit'),'source':a.get('source'),'status':a.get('status','RECORDED'),'notes':a.get('notes'),'audit':[{'at':ts,'event':'CREATED'}]}
        records[record_id]=record; save_usage(records); return record
    if name=='list_usage':
        category=a.get('category'); status=a.get('status')
        rows=list(records.values())
        if category is not None: rows=[r for r in rows if r.get('category')==category]
        if status is not None: rows=[r for r in rows if r.get('status')==status]
        rows.sort(key=lambda r:r.get('created_at',''),reverse=True)
        return {'count':len(rows),'records':rows}
    if name=='update_usage':
        uid=a.get('usage_id')
        if not isinstance(uid,str) or uid not in records: err('USAGE_RECORD_NOT_FOUND')
        updates=a.get('updates')
        if not isinstance(updates,dict) or not updates: err('USAGE_UPDATES_REQUIRED')
        allowed={'category','action','value','unit','source','status','notes'}
        unknown=set(updates)-allowed
        if unknown: err('INVALID_USAGE_FIELDS:'+','.join(sorted(unknown)))
        if 'category' in updates and (not isinstance(updates['category'],str) or not updates['category'].strip()): err('USAGE_CATEGORY_REQUIRED')
        if 'action' in updates and (not isinstance(updates['action'],str) or not updates['action'].strip()): err('USAGE_ACTION_REQUIRED')
        if 'value' in updates and updates['value'] is None: err('USAGE_VALUE_REQUIRED')
        rec=records[uid]
        for k,v in updates.items(): rec[k]=v.strip() if k in ('category','action') and isinstance(v,str) else v
        ts=now(); rec['updated_at']=ts; rec.setdefault('audit',[]).append({'at':ts,'event':'UPDATED','fields':sorted(updates.keys())})
        records[uid]=rec; save_usage(records); return rec
    return None

def handle(name,a):
    if name in {'record_usage','list_usage','update_usage'}: return usage_handle(name,a)
    tasks=load()
    if name=='create_task':
        tid=str(uuid.uuid4()); t={'task_id':tid,'attempt_id':None,'status':'RECEIVED','current_step':1,'input':a.get('input',{}),'original_task_input':a.get('input',{}),'evidence':[],'findings':[],'plan':[],'execution':[],'verification':[],'route':{},'errors':[],'audit':[]}
        new_attempt(t,t['original_task_input']); tasks[tid]=t; save(tasks); return t
    tid=a.get('task_id'); t=get_task(tasks,tid)
    if name=='get_task': return t
    if name=='get_audit': return t['audit']
    if name=='reset_task':
        reason=a.get('reason','UNSPECIFIED'); prev=t['attempt_id']; t['errors'].append({'at':now(),'reason':reason,'attempt_id':prev}); t['audit'].append({'at':now(),'event':'RESET','reason':reason,'previous_attempt_id':prev}); new_attempt(t,t['original_task_input']); save(tasks); return t
    step=int(name.split('_')[-1]) if name.startswith('step_') else None
    if step:
        require_step(t,step)
        if step==1:
            t['status']='ANALYZING'; t['input']=a.get('input',t['input']); result={'step':1,'status':'PASS','result':{'accepted':True}}
        elif step==2:
            ev=a.get('evidence',[])
            for e in ev:
                if e.get('source_type') not in ALLOWED_EVIDENCE: err('INVALID_EVIDENCE_SOURCE_TYPE')
                if not e.get('source') or not e.get('content_hash') or not e.get('retrieved_at'): err('INCOMPLETE_EVIDENCE')
                e['verified']=True
            t['evidence']=ev; t['findings']=a.get('findings',[]); t['plan']=a.get('plan',[]); t['status']='VALIDATING'; result={'step':2,'status':'PASS','result':{'evidence_count':len(ev),'finding_count':len(t['findings'])}}
        elif step==3:
            refs=set(e['evidence_id'] for e in t['evidence'] if e.get('verified'))
            bad=[r for r in a.get('evidence_refs',[]) if r not in refs]
            if bad: t['audit'].append({'at':now(),'event':'VALIDATION_FAIL','bad_evidence_refs':bad}); save(tasks); return {'step':3,'status':'FAIL','error':'EVIDENCE_REFERENCE_INVALID','reset_required':True}
            t['route']=a.get('proposed_route',{}); t['status']='EXECUTING'; result={'step':3,'status':'PASS','result':{'validated':True},'proposed_route':t['route']}
        elif step==4:
            if t['status']!='EXECUTING': err('EXECUTION_NOT_AUTHORIZED')
            t['execution']=a.get('execution',[]); t['status']='VERIFYING'; result={'step':4,'status':'PASS','result':{'executed':True}}
        else:
            passed=bool(a.get('passed'))
            t['verification']=a.get('verification',[])
            if passed: t['status']='COMPLETED'; t['current_step']=5; result={'step':5,'status':'PASS','result':{'completed':True}}
            else: result={'step':5,'status':'FAIL','result':{'completed':False},'reset_required':True}
        if step<5: t['current_step']=step+1
        t['audit'].append({'at':now(),'event':f'STEP_{step}','status':result['status'],'attempt_id':t['attempt_id']}); save(tasks); return result
    err('UNKNOWN_TOOL')

def reply(i,r=None,e=None):
    out={'jsonrpc':'2.0','id':i}
    out['result']=r if e is None else {'isError':True,'content':[{'type':'text','text':e}]}
    print(json.dumps(out,ensure_ascii=False),flush=True)
def main():
    for line in sys.stdin:
        try:
            q=json.loads(line); i=q.get('id'); m=q.get('method'); p=q.get('params',{}) or {}
            if m=='initialize': reply(i,{'protocolVersion':'2024-11-05','capabilities':{'tools':{}},'serverInfo':{'name':'chatgpt-control-api','version':'0.2.1'}})
            elif m=='notifications/initialized': continue
            elif m=='tools/list':
                definitions=[
                    ('create_task','Create an isolated controlled task',{'input':'object'}),('get_task','Get current task state',{'task_id':'string'}),('get_audit','Get task audit trail',{'task_id':'string'}),('reset_task','Reset task to a new attempt at Step 1',{'task_id':'string','reason':'string'}),
                    ('step_1','Receive and analyze task input',{'task_id':'string','input':'object'}),('step_2','Analyze and research with current evidence',{'task_id':'string','evidence':'array','findings':'array','plan':'array'}),('step_3','Validate evidence, consistency, and route',{'task_id':'string','evidence_refs':'array','proposed_route':'object'}),('step_4','Execute approved plan',{'task_id':'string','execution':'array'}),('step_5','Verify execution result',{'task_id':'string','passed':'boolean','verification':'array'}),
                    ('record_usage','Create a usage-data record',{'category':'string','action':'string','value':'any','unit':'string','source':'string','status':'string','notes':'string'}),('list_usage','List usage records with optional category/status filters',{'category':'string','status':'string'}),('update_usage','Update an existing usage record by exact ID',{'usage_id':'string','updates':'object'})]
                tools=[]
                for n,d,props in definitions:
                    schema={'type':'object','properties':{k:({'type':v} if v in ('string','object','array','boolean') else {}) for k,v in props.items()},'additionalProperties':False}
                    required={'create_task':['input'],'get_task':['task_id'],'get_audit':['task_id'],'reset_task':['task_id'],'step_1':['task_id'],'step_2':['task_id'],'step_3':['task_id'],'step_4':['task_id'],'step_5':['task_id','passed'],'record_usage':['category','action','value'],'list_usage':[],'update_usage':['usage_id','updates']}[n]
                    schema['required']=required
                    if n=='update_usage': schema['properties']['updates']={'type':'object'}
                    tools.append({'name':n,'description':d,'inputSchema':schema})
                reply(i,{'tools':tools})
            elif m=='tools/call':
                n=p.get('name'); a=p.get('arguments',{}) or {}
                try: r=handle(n,a); reply(i,{'content':[{'type':'text','text':json.dumps(r,ensure_ascii=False)}]})
                except Exception as ex: reply(i,None,str(ex))
            else: reply(i,{})
        except Exception as ex:
            try: reply(None,None,str(ex))
            except Exception: pass
if __name__=='__main__': main()
