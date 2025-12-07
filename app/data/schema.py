import pandas as pd
from app.data.db import connect_database
from pathlib import Path

# paths
CYBER_CSV = Path("DATA") / "cyber_incidents.csv"
TICKETS_CSV = Path("DATA") / "it_tickets.csv"
DATASETS_CSV = Path("DATA") / "datasets_metadata.csv"


def create_tables():
    conn = connect_database()
    cur = conn.cursor()

    # users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash BLOB NOT NULL,
            role TEXT NOT NULL
        )
    """)

    # cyber incidents table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cyber_incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            incident_id INTEGER,
            timestamp TEXT,
            severity TEXT,
            category TEXT,
            status TEXT,
            description TEXT
        )
    """)

    # IT tickets table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS it_tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id INTEGER,
            priority TEXT,
            description TEXT,
            status TEXT,
            assigned_to TEXT,
            created_at TEXT,
            resolution_time_hours REAL
        )
    """)

    # datasets metadata table (full info from CSV)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS datasets_metadata (
            dataset_id INTEGER,
            name TEXT,
            rows INTEGER,
            columns INTEGER,
            uploaded_by TEXT,
            upload_date TEXT
        )
    """)

    # datasets table (simple for dashboard)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS datasets_metadata (
            dataset_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            rows INTEGER,
            columns INTEGER,
            uploaded_by TEXT,
            upload_date TEXT
        )
    """)

    conn.commit()
    conn.close()


def load_csv_if_empty():
    conn = connect_database()

    # cyber incidents
    df1 = pd.read_csv(CYBER_CSV)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM cyber_incidents")
    if cur.fetchone()[0] == 0:
        df1.to_sql("cyber_incidents", conn, if_exists="append", index=False)

    # tickets
    df2 = pd.read_csv(TICKETS_CSV)
    cur.execute("SELECT COUNT(*) FROM it_tickets")
    if cur.fetchone()[0] == 0:
        df2.to_sql("it_tickets", conn, if_exists="append", index=False)

    # datasets metadata
    df3 = pd.read_csv(DATASETS_CSV)
    cur.execute("SELECT COUNT(*) FROM datasets_metadata")
    if cur.fetchone()[0] == 0:
        df3.to_sql("datasets_metadata", conn, if_exists="append", index=False)



    conn.close()
