from database import get_db
ACTIVE_PROJECT_STATUSES = {"ACTIVE", "IN_PROGRESS"}
ALLOWED_PHASES = {"MCR", "SRR", "PDR", "CDR", "TRR", "ORR"}
def check_project(project_id: int):
    conn = get_db()
    try:
        row = conn.execute("SELECT * FROM projects WHERE id=?", (project_id,)).fetchone()
        if row is None: return False, "project not found"
        if row["status"] not in ACTIVE_PROJECT_STATUSES: return False, "project is not active"
        return True, "ok"
    finally: conn.close()
def check_budget(project_id: int, amount: float = 0.0):
    conn = get_db()
    try:
        rows = conn.execute('SELECT used,"limit" FROM budget WHERE project_id=?', (project_id,)).fetchall()
        for row in rows:
            if row["limit"] is not None and float(row["used"] or 0) + amount > float(row["limit"]): return False, "budget exceeded"
        return True, "ok"
    finally: conn.close()
def check_phase(phase):
    return phase in ALLOWED_PHASES, ("ok" if phase in ALLOWED_PHASES else "invalid phase")
