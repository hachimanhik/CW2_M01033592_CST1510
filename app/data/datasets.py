import pandas as pd

# get all datasets
def get_all_datasets(conn):
    cur = conn.cursor()
    cur.execute("SELECT dataset_id, name, rows FROM datasets_metadata")
    rows = cur.fetchall()
    df = pd.DataFrame(rows, columns=["id", "name", "rows"])
    return df

# insert new dataset
def insert_dataset(conn, name, rows):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO datasets_metadata (name, rows, columns, uploaded_by, upload_date) VALUES (?, ?, ?, ?, ?)",
        (name, rows, 0, "system", "2025-01-01")
    )
    conn.commit()

# delete dataset
def delete_dataset(conn, dataset_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM datasets_metadata WHERE dataset_id = ?", (dataset_id,))
    conn.commit()
