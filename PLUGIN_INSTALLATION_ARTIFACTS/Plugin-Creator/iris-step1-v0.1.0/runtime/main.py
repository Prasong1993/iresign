from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_db, init_db, load_seed_data
from task_queue import create_task
app = FastAPI(title="IRIS Backend Controller", version="0.1.0")
class ProjectIn(BaseModel):
    name: str
    description: str | None = None
    budget: float | None = None
class TaskIn(BaseModel):
    title: str
    phase: str | None = None
@app.on_event("startup")
def startup(): init_db(); load_seed_data()
@app.get("/")
def root(): return {"status": "IRIS running"}
@app.get("/health")
def health(): return {"status": "ok"}
@app.post("/projects")
def create_project(body: ProjectIn):
    conn = get_db()
    try:
        cur = conn.execute("INSERT INTO projects(name,description,budget,current_phase) VALUES(?,?,?,?)", (body.name, body.description, body.budget, "MCR"))
        project_id = cur.lastrowid
        conn.execute("INSERT INTO audit_log(actor,action,details) VALUES(?,?,?)", ("ChatGPT", "PROJECT_CREATED", f"project_id={project_id}"))
        conn.commit()
        return {"id": project_id, "name": body.name, "status": "ACTIVE", "current_phase": "MCR"}
    finally: conn.close()
@app.get("/projects/{project_id}")
def get_project(project_id: int):
    conn = get_db()
    try:
        row = conn.execute("SELECT * FROM projects WHERE id=?", (project_id,)).fetchone()
        if row is None: raise HTTPException(404, "project not found")
        return dict(row)
    finally: conn.close()
@app.post("/projects/{project_id}/tasks")
def create_project_task(project_id: int, body: TaskIn):
    try: return {"id": create_task(project_id, body.title, body.phase), "status": "QUEUED"}
    except ValueError as exc: raise HTTPException(400, str(exc))
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    conn = get_db()
    try:
        row = conn.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
        if row is None: raise HTTPException(404, "task not found")
        return dict(row)
    finally: conn.close()
@app.get("/audit")
def audit():
    conn = get_db()
    try: return [dict(row) for row in conn.execute("SELECT * FROM audit_log ORDER BY id")]
    finally: conn.close()
