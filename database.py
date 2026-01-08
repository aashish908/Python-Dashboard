import mysql.connector

# ----------------------------
# MYSQL CONFIG
# ----------------------------
DB_CONFIG = {
    "host": "localhost",        # e.g. localhost or server IP
    "user": "root",             # your mysql username
    "password": "Era@123$",
    "database": "dashboard_db"  # database name
}

# ----------------------------
# DB CONNECTION
# ----------------------------
def get_db():
    return mysql.connector.connect(**DB_CONFIG)

# ----------------------------
# CREATE USERS TABLE
# ----------------------------
def create_users_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# ----------------------------
# VALIDATE LOGIN
# ----------------------------
def validate_user(username, password):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, username FROM users WHERE username=%s AND password=%s",
        (username, password)
    )
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

# ----------------------------
# REGISTER USER
# ----------------------------
def create_user(username, password, email):
    conn = get_db()
    cursor = conn.cursor()

    # check duplicate username or email
    cursor.execute(
        "SELECT id FROM users WHERE username=%s OR email=%s",
        (username, email)
    )
    if cursor.fetchone():
        cursor.close()
        conn.close()
        raise Exception("Username or Email already exists")

    cursor.execute(
        "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
        (username, password, email)
    )

    conn.commit()
    cursor.close()
    conn.close()
