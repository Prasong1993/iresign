"""IRIS MCP server with persisted execution telemetry."""
import asyncio, json, sys, uuid
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import database
from controller import create_work, run_step, get_work, record_error, checkpoint
from model import STEP_DEFINITIONS, StepStatus
from tool_registry import ToolEntry, ToolRegistry, ToolState
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

APP_VERSION = "0.6.16"
server = Server("iris-controller")
tool_registry = ToolRegistry()

def ok(data):
    return [TextContent(type="text", text=json.dumps({"status":"OK","version":APP_VERSION,**data},ensure_ascii=False,default=str))]
def err(kind,message,**extra):
    return [TextContent(type="text",text=json.dumps({"status":"ERROR","error_type":kind,"message":message,**extra},ensure_ascii=False,default=str))]

TOOLS = [
 Tool(name="health",description="Initialize and verify the SQLite database connection.",inputSchema={"type":"object","properties":{}}),
 Tool(name="runtime_status",description="Read persisted runtime events, latest checkpoint/error/verification, and active tool calls.",inputSchema={"type":"object","properties":{"work_id":{"type":"string"}}}),
 Tool(name="create_work",description="Create a new IRIS work unit.",inputSchema={"type":"object","properties":{"work_id":{"type":"string"},"title":{"type":"string"}},"required":["work_id","title"]}),
 Tool(name="run_step",description="Run a deterministic gated step; the prior step must have passed.",inputSchema={"type":"object","properties":{"work_id":{"type":"string"},"step":{"type":"integer","minimum":1,"maximum":5},"expected":{"type":"string"},"actual":{"type":"string"},"note":{"type":"string"},"fail_attempts":{"type":"integer","minimum":0,"maximum":9},"max_attempts":{"type":"integer","minimum":1,"maximum":10}},"required":["work_id","step","expected","actual"]}),
 Tool(name="final_verify",description="Final expected-vs-actual verification; requires all five steps to PASS.",inputSchema={"type":"object","properties":{"work_id":{"type":"string"},"expected":{"type":"string"},"actual":{"type":"string"},"note":{"type":"string"}},"required":["work_id","expected","actual"]}),
 Tool(name="get_work_status",description="Read work, steps, errors, checkpoints, audit, verifications, events and tool calls.",inputSchema={"type":"object","properties":{"work_id":{"type":"string"}},"required":["work_id"]}),
 Tool(name="add_evidence",description="Persist one evidence record.",inputSchema={"type":"object","properties":{"id":{"type":"string"},"status":{"type":"string"},"topic":{"type":"string"},"fact":{"type":"string"},"source":{"type":"string"},"verification_state":{"type":"string"}},"required":["id","status","topic","fact","source","verification_state"]}),
 Tool(name="list_evidence",description="List persisted evidence.",inputSchema={"type":"object","properties":{}}),
 Tool(name="register_tool",description="Register a tool explicitly exposed by a real adapter. Registration does not invoke it.",inputSchema={"type":"object","properties":{"tool_id":{"type":"string"},"provider":{"type":"string"},"capabilities":{"type":"array","items":{"type":"string"}},"state":{"type":"string","enum":["AVAILABLE","QUOTA_EXHAUSTED","UNAUTHORIZED","UNAVAILABLE","UNKNOWN"]},"free_tier":{"type":"boolean"},"priority":{"type":"integer"},"daily_quota_remaining":{"type":["integer","null"]},"cost_per_call":{"type":"number"},"requires_auth":{"type":"boolean"}},"required":["tool_id","provider","capabilities"]}),
 Tool(name="list_registered_tools",description="List tools registered in this server process; does not discover all ChatGPT tools.",inputSchema={"type":"object","properties":{}}),
 Tool(name="update_tool_state",description="Update a registered tool state from real adapter evidence.",inputSchema={"type":"object","properties":{"tool_id":{"type":"string"},"state":{"type":"string","enum":["AVAILABLE","QUOTA_EXHAUSTED","UNAUTHORIZED","UNAVAILABLE","UNKNOWN"]},"quota_remaining":{"type":["integer","null"]}},"required":["tool_id","state"]}),
 Tool(name="route_tool",description="Select an eligible registered tool. Selection does not invoke an external provider.",inputSchema={"type":"object","properties":{"capability":{"type":"string"},"paid_allowed":{"type":"boolean"},"budget_remaining":{"type":"number"}},"required":["capability"]})
]

@server.list_tools()
async def list_tools():
    return TOOLS

async def _dispatch(name, a):
    if name == "health":
        database.init_db()
        with database.get_connection() as c: c.execute("SELECT 1").fetchone()
        return ok({"database":"ok","db_path":str(database.get_db_path())})
    if name == "runtime_status":
        wid = str(a.get("work_id","")).strip() or None
        result = database.runtime_status(wid)
        if wid:
            work = get_work(wid)
            if not work: return err("NOT_FOUND",f"work {wid} not found")
            result["work"] = work["work"]; result["steps"] = work["steps"]
        return ok(result)
    if name == "create_work":
        wid,title=str(a.get("work_id","")).strip(),str(a.get("title","")).strip()
        if not wid or not title: return err("VALIDATION","work_id and title are required")
        try: create_work(wid,title)
        except Exception as e: return err("CONFLICT" if "UNIQUE" in str(e) else "INTERNAL",str(e))
        return ok({"work_id":wid,"title":title,"work_status":"CREATED"})
    if name == "run_step":
        try:
            result=run_step(str(a["work_id"]),int(a["step"]),str(a["expected"]),str(a["actual"]),
                str(a.get("note",""))[:2000],int(a.get("fail_attempts",0)),int(a.get("max_attempts",10)))
            return ok(result)
        except ValueError as e: return err("GATE_VIOLATION",str(e))
        except RuntimeError as e: return err("ATTEMPTS_EXHAUSTED",str(e))
    if name == "final_verify":
        wid=str(a.get("work_id","")).strip()
        result=get_work(wid)
        if not result: return err("NOT_FOUND",f"work {wid} not found")
        latest={}
        for row in result["steps"]: latest[row["step"]]=row
        missing=[i for i in STEP_DEFINITIONS if latest.get(i,{}).get("status")!=StepStatus.PASSED.value]
        if missing: return err("GATE_VIOLATION",f"all five steps must PASS; missing/failed {missing}")
        expected,actual=str(a.get("expected","")),str(a.get("actual",""))
        status="VERIFIED" if expected.strip()==actual.strip() else "MISMATCH"
        with database.get_connection() as c:
            c.execute("INSERT INTO verifications(work_id,expected,actual,status,note) VALUES(?,?,?,?,?)",(wid,expected,actual,status,str(a.get("note",""))[:2000]))
            c.execute("INSERT INTO audit_log(work_id,action,details) VALUES(?,?,?)",(wid,"FINAL_VERIFICATION",status))
            if status=="VERIFIED": c.execute("UPDATE work_units SET status='DELIVERED',updated_at=CURRENT_TIMESTAMP WHERE id=?",(wid,))
        database.record_event("VERIFICATION_PASSED" if status=="VERIFIED" else "VERIFICATION_FAILED",work_id=wid,status=status,payload={"expected":expected,"actual":actual})
        if status!="VERIFIED":
            record_error(wid,0,0,"FINAL_VERIFICATION_MISMATCH","expected and actual differ",expected,actual,"MISMATCH","work not delivered","correct result and retry","MISMATCH","never promote mismatch to VERIFIED")
            checkpoint(wid,0,"FINAL_MISMATCH",{"expected":expected,"actual":actual,"retained":True})
            return err("FINAL_MISMATCH","verification mismatch retained in database",persisted=True)
        return ok({"verification_status":"VERIFIED","work_id":wid,"delivered":True})
    if name == "get_work_status":
        wid=str(a.get("work_id","")).strip()
        result=get_work(wid) if wid else None
        if not result: return err("NOT_FOUND" if wid else "VALIDATION",f"work {wid} not found" if wid else "work_id required")
        return ok({"work_id":wid,"work_status":result["work"]["status"],**result})
    if name == "add_evidence":
        keys=("id","status","topic","fact","source","verification_state")
        vals=tuple(str(a.get(k,"")).strip() for k in keys)
        if any(not x for x in vals): return err("VALIDATION","all evidence fields are required")
        try:
            with database.get_connection() as c: c.execute("INSERT INTO evidence(id,status,topic,fact,source,verification_state) VALUES(?,?,?,?,?,?)",vals)
            database.record_event("EVIDENCE_COLLECTED",status=vals[1],payload={"evidence_id":vals[0],"source":vals[4],"verification_state":vals[5]})
            return ok({"evidence_id":vals[0],"recorded":True})
        except Exception as e: return err("CONFLICT" if "UNIQUE" in str(e) else "INTERNAL",str(e))
    if name == "list_evidence":
        items=database.many("SELECT * FROM evidence ORDER BY created_at,id")
        return ok({"items":items,"count":len(items)})
    if name == "register_tool":
        try:
            tid=str(a.get("tool_id","")).strip(); provider=str(a.get("provider","")).strip()
            caps=a.get("capabilities",[])
            if not tid or not provider or not isinstance(caps,list) or not caps: return err("VALIDATION","tool_id, provider, capabilities required")
            state=ToolState(str(a.get("state","UNKNOWN")))
            entry=ToolEntry(tid,provider,frozenset(str(c).strip() for c in caps),state,bool(a.get("free_tier",True)),int(a.get("priority",100)),a.get("daily_quota_remaining"),float(a.get("cost_per_call",0)),bool(a.get("requires_auth",True)))
            if entry.cost_per_call<0: return err("VALIDATION","cost_per_call must be >= 0")
            tool_registry.register(entry)
            database.record_event("TOOL_REGISTERED",status=state.value,payload={"tool_id":tid,"provider":provider,"capabilities":caps})
            return ok({"tool_id":tid,"registered":True,"state":state.value,"external_invocation":"not_implemented"})
        except (ValueError,TypeError) as e: return err("VALIDATION",str(e))
    if name == "list_registered_tools":
        return ok({"items":[{"tool_id":e.tool_id,"provider":e.provider,"capabilities":sorted(e.capabilities),"state":e.state.value,"free_tier":e.free_tier,"priority":e.priority,"daily_quota_remaining":e.daily_quota_remaining,"cost_per_call":e.cost_per_call} for e in tool_registry.list_entries()],"process_scope":"in-memory","automatic_host_discovery":False})
    if name == "update_tool_state":
        try:
            tid=str(a["tool_id"]); state=ToolState(str(a["state"]))
            quota=a.get("quota_remaining")
            tool_registry.update_state(tid,state,quota_remaining=int(quota) if quota is not None else None)
            database.record_event("TOOL_STATE_UPDATED",status=state.value,payload={"tool_id":tid,"quota_remaining":quota})
            return ok({"tool_id":tid,"state":state.value})
        except KeyError as e: return err("NOT_FOUND",str(e))
        except (ValueError,TypeError) as e: return err("VALIDATION",str(e))
    if name == "route_tool":
        cap=str(a.get("capability","")).strip()
        if not cap: return err("VALIDATION","capability required")
        try:
            d=tool_registry.choose(cap,paid_allowed=bool(a.get("paid_allowed",False)),budget_remaining=float(a.get("budget_remaining",0)))
            selected=d.selected
            return ok({"capability":cap,"reason":d.reason,"selected":({"tool_id":selected.tool_id,"provider":selected.provider,"free_tier":selected.free_tier,"cost_per_call":selected.cost_per_call} if selected else None),"candidates":list(d.candidates),"skipped":[{"tool_id":x,"reason":y} for x,y in d.skipped],"invocation_performed":False})
        except (ValueError,TypeError) as e: return err("VALIDATION",str(e))
    return err("UNKNOWN_TOOL",f"tool {name} is not implemented")

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    database.init_db()
    tool_call_id, trace_id = str(uuid.uuid4()), str(uuid.uuid4())
    work_id = str(arguments.get("work_id","")).strip() or None
    started = False
    side_effecting = name in {"create_work", "run_step", "final_verify", "add_evidence", "register_tool", "update_tool_state"}
    try:
        with database.get_connection() as c:
            c.execute("INSERT INTO tool_calls(tool_call_id,work_id,trace_id,tool_name,status,input_json,started_at,side_effect_started) VALUES(?,?,?,?,?,?,CURRENT_TIMESTAMP,?)",
                      (tool_call_id,work_id,trace_id,name,"RUNNING",json.dumps(arguments,ensure_ascii=False,sort_keys=True),int(side_effecting)))
        started=True
        database.record_event("TOOL_STARTED",work_id=work_id,trace_id=trace_id,tool_call_id=tool_call_id,status="RUNNING",payload={"tool_name":name,"arguments":arguments})
        result=await _dispatch(name,arguments or {})
        parsed={}
        try: parsed=json.loads(result[0].text)
        except Exception: parsed={"status":"UNKNOWN"}
        succeeded=parsed.get("status")=="OK"
        final_status="SUCCEEDED" if succeeded else "FAILED"
        with database.get_connection() as c:
            c.execute("UPDATE tool_calls SET status=?,output_json=?,error_json=?,finished_at=CURRENT_TIMESTAMP,result_recorded_at=CURRENT_TIMESTAMP WHERE tool_call_id=?",
                (final_status,json.dumps(parsed,ensure_ascii=False,sort_keys=True) if succeeded else None,
                 None if succeeded else json.dumps(parsed,ensure_ascii=False,sort_keys=True),tool_call_id))
        database.record_event("TOOL_RESULT_RECEIVED",work_id=work_id,trace_id=trace_id,tool_call_id=tool_call_id,status=final_status,payload={"tool_name":name,"result_status":parsed.get("status"),"error_type":parsed.get("error_type")})
        database.record_event("TOOL_SUCCEEDED" if succeeded else "TOOL_FAILED",work_id=work_id,trace_id=trace_id,tool_call_id=tool_call_id,status=final_status,payload={"tool_name":name})
        return result
    except Exception as exc:
        if started:
            try:
                with database.get_connection() as c:
                    c.execute("UPDATE tool_calls SET status='FAILED',error_json=?,finished_at=CURRENT_TIMESTAMP WHERE tool_call_id=?",(json.dumps({"type":type(exc).__name__,"message":str(exc)}),tool_call_id))
                database.record_event("TOOL_FAILED",work_id=work_id,trace_id=trace_id,tool_call_id=tool_call_id,status="FAILED",payload={"tool_name":name,"error":str(exc)})
            except Exception:
                pass
        return err("INTERNAL",f"tool dispatch failed: {type(exc).__name__}: {exc}",tool_call_id=tool_call_id)

async def main():
    database.init_db()
    async with stdio_server() as (reader,writer):
        await server.run(reader,writer,server.create_initialization_options())

if __name__=="__main__":
    asyncio.run(main())
