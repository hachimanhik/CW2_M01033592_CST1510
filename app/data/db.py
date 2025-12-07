from pathlib import Path
import sqlite3

DB_PATH = Path("DATA") / "intelligence_platform.db"

def connect_database():
    # create DATA folder if missing
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
