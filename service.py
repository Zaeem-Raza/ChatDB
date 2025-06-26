# service.py

import sqlite3
from User import User

DB_NAME = "users.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insert_user(user: User) -> str:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (user.name, user.age))
    conn.commit()
    conn.close()
    return f"{user.name}, age {user.age}, has been added to the database."

# Optional: Add more functions later
def get_all_users() -> list[User]:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, age FROM users")
    rows = cursor.fetchall()
    conn.close()
    return [User(name=row[0], age=row[1]) for row in rows]
