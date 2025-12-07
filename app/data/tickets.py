import pandas as pd


def get_all_tickets(conn) -> pd.DataFrame:
    """Return all IT tickets as DataFrame."""
    query = """
        SELECT id, ticket_id, priority, description, status,
               assigned_to, created_at, resolution_time_hours
        FROM it_tickets
        ORDER BY created_at
    """
    return pd.read_sql_query(query, conn)


def insert_ticket(
    conn,
    ticket_id,
    priority,
    description,
    status,

    assigned_to,
    created_at,
    resolution_time_hours,
):
    """Add new ticket row."""
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO it_tickets
        (ticket_id, priority, description, status,
         assigned_to, created_at, resolution_time_hours)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            ticket_id,
            priority,
            description,
            status,
            assigned_to,
            created_at,
            resolution_time_hours,
        ),
    )
    conn.commit()


def update_ticket_status(conn, row_id, new_status):
    """Update status for one ticket."""
    cur = conn.cursor()
    cur.execute(
        "UPDATE it_tickets SET status = ? WHERE id = ?",
        (new_status, row_id),
    )
    conn.commit()


def delete_ticket(conn, row_id):
    """Delete one ticket."""
    cur = conn.cursor()
    cur.execute("DELETE FROM it_tickets WHERE id = ?", (row_id,))
    conn.commit()
