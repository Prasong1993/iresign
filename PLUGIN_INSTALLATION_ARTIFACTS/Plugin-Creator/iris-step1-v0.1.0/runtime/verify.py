import re
from database import get_db
from policy import check_project, check_budget, check_phase

def verify_task(project_id: int, title: str, phase: str | None = None, output: str | None = None, budget_amount: float = 0.0):
    errors = []
    ok, msg = check_project(project_id)
    if not ok: errors.append(msg)
    ok, msg = check_budget(project_id, budget_amount)
    if not ok: errors.append(msg)
    if phase:
        ok, msg = check_phase(phase)
        if not ok: errors.append(msg)
    conn = get_db()
    try:
        duplicate = conn.execute("SELECT id FROM tasks WHERE project_id=? AND title=? AND status IN ('COMPLETED','RUNNING','QUEUED')", (project_id, title)).fetchone()
        if duplicate and "re-run" not in title.lower(): errors.append("duplicate task")
    finally: conn.close()
    if output:
        for match in re.finditer(r"```(?:\w+)?\n", output):
            if match.group(0) == "```\n": errors.append("code block language is missing")
    return {"passed": not errors, "errors": errors}

def verify_until_clean(check_fn, max_rounds=10):
    history = []
    for round_no in range(1, max_rounds + 1):
        result = check_fn()
        history.append({"round": round_no, "result": result})
        if result.get("passed"): return {"passed": True, "rounds": history}
    return {"passed": False, "rounds": history, "reason": "verification did not become clean within configured rounds"}
