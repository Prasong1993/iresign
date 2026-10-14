import json
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "iris.db"
SEED_DIR = BASE_DIR / "seed"

def get_db():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    try:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT, status TEXT NOT NULL DEFAULT 'ACTIVE', budget REAL, current_phase TEXT, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
        CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, project_id INTEGER NOT NULL, title TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'QUEUED', phase TEXT, tool_used TEXT, attempt INTEGER NOT NULL DEFAULT 0, result TEXT, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(project_id) REFERENCES projects(id));
        CREATE TABLE IF NOT EXISTS decisions (id INTEGER PRIMARY KEY AUTOINCREMENT, project_id INTEGER NOT NULL, decision TEXT NOT NULL, decided_by TEXT, context TEXT, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(project_id) REFERENCES projects(id));
        CREATE TABLE IF NOT EXISTS knowledge (id INTEGER PRIMARY KEY AUTOINCREMENT, key TEXT NOT NULL, content TEXT NOT NULL, source TEXT, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
        CREATE TABLE IF NOT EXISTS patterns (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, category TEXT, content TEXT NOT NULL, version TEXT, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
        CREATE TABLE IF NOT EXISTS errors (id INTEGER PRIMARY KEY AUTOINCREMENT, pattern TEXT NOT NULL, root_cause TEXT, fix TEXT, prevention_rule TEXT, source TEXT, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
        CREATE TABLE IF NOT EXISTS tools (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, purpose TEXT, tier TEXT, status TEXT, endpoint TEXT, notes TEXT, last_tested TEXT);
        CREATE TABLE IF NOT EXISTS risks (id INTEGER PRIMARY KEY AUTOINCREMENT, project_id INTEGER NOT NULL, risk TEXT NOT NULL, probability TEXT, impact TEXT, mitigation TEXT, status TEXT, FOREIGN KEY(project_id) REFERENCES projects(id));
        CREATE TABLE IF NOT EXISTS audit_log (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, actor TEXT, action TEXT NOT NULL, details TEXT, task_id INTEGER, FOREIGN KEY(task_id) REFERENCES tasks(id));
        CREATE TABLE IF NOT EXISTS budget (id INTEGER PRIMARY KEY AUTOINCREMENT, project_id INTEGER NOT NULL, resource TEXT NOT NULL, used REAL NOT NULL DEFAULT 0, "limit" REAL, unit TEXT, FOREIGN KEY(project_id) REFERENCES projects(id));
        """)
        conn.commit()
    finally:
        conn.close()

def load_seed_data():
    init_db()
    conn = get_db()
    try:
        sources = [
            ("errors_nasa.json", "errors", ("pattern","root_cause","fix","prevention_rule","source")),
            ("tools.json", "tools", ("name","purpose","tier","status","endpoint","notes","last_tested")),
            ("patterns.json", "patterns", ("name","category","content","version")),
        ]
        for filename, table, cols in sources:
            path = SEED_DIR / filename
            if not path.exists():
                continue
            rows = json.loads(path.read_text(encoding="utf-8"))
            for row in rows:
                values = [row.get(c) for c in cols]
                marks = ",".join("?" for _ in cols)
                conn.execute(f"INSERT INTO {table} ({','.join(cols)}) VALUES ({marks})", values)
        conn.commit()
    finally:
        conn.close()
