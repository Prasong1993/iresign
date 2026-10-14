from database import get_db
from verify import verify_task
MAX_ATTEMPTS = 3
def choose_tool(title: str):
    text = title.lower()
    if any(k in text for k in ("web", "url", "search")): return "web"
    if any(k in text for k in ("file", "ไฟล์", "folder")): return "filesystem"
    return "default"
def create_task(project_id: int, title: str, phase: str | None = None):
    verification = verify_task(project_id, title, phase)
    if not verification["passed"]: raise ValueError("; ".join(verification["errors"]))
    conn = get_db()
    try:
        tool = choose_tool(title)
        cur = conn.execute("INSERT INTO tasks(project_id,title,phase,status,tool_used) VALUES(?,?,?,?,?)", (project_id,title,phase,"QUEUED",tool))
        task_id = cur.lastrowid
        conn.execute("INSERT INTO audit_log(actor,action,details,task_id) VALUES(?,?,?,?)", ("IRIS","TASK_CREATED",f"tool={tool}",task_id))
        conn.commit()
        return task_id
    finally: conn.close()
