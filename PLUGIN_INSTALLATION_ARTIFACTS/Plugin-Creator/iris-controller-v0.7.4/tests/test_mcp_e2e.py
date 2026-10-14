import asyncio, json, tempfile
from pathlib import Path
from runtime.mcp_server import call_tool
import database

def call(name, **args):
    return json.loads(asyncio.run(call_tool(name, args))[0].text)

def test_mcp_full_e2e():
    database.set_db_path(Path(tempfile.mkdtemp()) / "iris_mcp_e2e.db")
    database.init_db(); wid="mcp-e2e-068"
    assert call("create_work", work_id=wid, title="MCP E2E")["status"] == "OK"
    for step in range(1,6): assert call("run_step", work_id=wid, step=step, expected=f"E{step}", actual=f"E{step}")["status"] == "OK"
    r=call("final_verify", work_id=wid, expected="MATCH", actual="MATCH")
    assert r["status"] == "OK" and r["verification_status"] == "VERIFIED"
    st=call("get_work_status", work_id=wid)
    assert st["status"] == "OK" and st["work"]["status"] == "DELIVERED"
