import sqlite3
import bcrypt
from app.data.db import connect_database


def register_user(username, password):
    # connect to database
    conn = connect_database()
    cur = conn.cursor()

    # hash password
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    try:
        cur.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
            (username, hashed, "user")
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def login_user(username, password):
    # connect to database
    conn = connect_database()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cur.fetchone()

    if user is None:
        return False

    # check password
    if bcrypt.checkpw(password.encode(), user["password_hash"]):
        return True

    return False
