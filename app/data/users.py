import bcrypt
from app.data.db import connect_database

def hash_password(password):
    # change password to bytes
    password_bytes = password.encode("utf-8")
    # create salt
    salt = bcrypt.gensalt()
    # make hash
    hash_bytes = bcrypt.hashpw(password_bytes, salt)
    # return string version
    return hash_bytes.decode("utf-8")

def create_user(conn, username, password, role = "user"):
    # make cursor
    cur = conn.cursor()
    # make hash
    password_hash = hash_password(password)

    # save user
    cur.execute(
        """
        INSERT INTO users (username, password_hash, role)
        VALUES (?, ?, ?)
        """,
        (username, password_hash, role),
    )
    conn.commit()

def get_user_by_username(conn, username):
    # find user by username
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cur.fetchone()

def verify_user(conn, username, password):
    # get user row
    row = get_user_by_username(conn, username)
    if row is None:
        return False, None

    # take saved hash
    stored_hash = row["password_hash"].encode("utf-8")
    # change password to bytes
    password_bytes = password.encode("utf-8")

    # check password
    if bcrypt.checkpw(password_bytes, stored_hash):
        return True, row["role"]

    return False, None
