"""Fresh isolated persistence checks for IRIS Control."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "runtime"))
import database

def test_additive_schema_and_event_round_trip(tmp_path, monkeypatch):
    db_path = tmp_path / "iris_test.db"
    monkeypatch.setenv("IRIS_DB_PATH", str(db_path))
    database.set_db_path(db_path)
    database.init_db()
    database.init_db()
    tables = {r["name"] for r in database.many("SELECT name FROM sqlite_master WHERE type='table'")}
    assert {"evidence","work_units","audit_log","schema_migrations","tool_calls","tool_registry","work_events","runtime_state","tasks","task_dependencies","policies","policy_decisions","recovery_points","verification_results"} <= tables
    database.record_event("TEST_EVENT", status="VERIFIED", payload={"test_fixture": True})
    state = database.runtime_status()
    assert state["database"] == "ok"
    assert state["latest_event"]["event_type"] == "TEST_EVENT"
    database.record_event("SECOND_TEST_EVENT", status="VERIFIED", payload={"sequence": 2})
    assert database.runtime_status()["latest_event"]["event_type"] == "SECOND_TEST_EVENT"
    assert json_payload(state["latest_event"]["payload_json"])["test_fixture"] is True
    assert database.one("SELECT version FROM schema_migrations WHERE version=1") is not None

def json_payload(value):
    import json
    return json.loads(value)
