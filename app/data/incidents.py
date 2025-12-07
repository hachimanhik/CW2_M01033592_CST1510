import pandas as pd


def get_all_incidents(conn):
    """Return all cyber incidents as DataFrame."""
    query = """
        SELECT id, incident_id, timestamp, severity, category, status, description
        FROM cyber_incidents
        ORDER BY timestamp
    """
    return pd.read_sql_query(query, conn)


def insert_incident(
    conn,
    incident_id,
    timestamp,
    severity,
    category,
    status,
    description,
):
    """Add new incident row."""
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO cyber_incidents
        (incident_id, timestamp, severity, category, status, description)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (incident_id, timestamp, severity, category, status, description),
    )
    conn.commit()


def update_incident_status(conn, row_id, new_status):
    """Update status for one incident."""
    cur = conn.cursor()
    cur.execute(
        "UPDATE cyber_incidents SET status = ? WHERE id = ?",
        (new_status, row_id),
    )
    conn.commit()


def delete_incident(conn, row_id):
    """Delete one incident."""
    cur = conn.cursor()
    cur.execute("DELETE FROM cyber_incidents WHERE id = ?", (row_id,))
    conn.commit()
