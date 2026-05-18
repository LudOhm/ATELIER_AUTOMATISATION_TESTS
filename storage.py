import sqlite3
import json


def init_db():
    conn = sqlite3.connect("runs.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS runs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        result TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_run(data):
    conn = sqlite3.connect("runs.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO runs(result) VALUES(?)",
        (json.dumps(data),)
    )

    conn.commit()
    conn.close()

