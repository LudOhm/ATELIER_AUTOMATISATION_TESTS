import sqlite3
import json

DB = "runs.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            data TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_run(run):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute(
        "INSERT INTO runs (timestamp, data) VALUES (?, ?)",
        (run["timestamp"], json.dumps(run))
    )
    conn.commit()
    conn.close()

def get_runs():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT timestamp, data FROM runs ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return [(t, json.loads(d)) for t, d in rows]