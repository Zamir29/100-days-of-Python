"""Day 63 — SQLite intro.

Goal: Create a local SQLite database file and a simple `books` table.
Note: This script is safe to re-run (uses IF NOT EXISTS).
"""

import sqlite3

db = sqlite3.connect("books-collection.db")

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title varchar(250) NOT NULL UNIQUE,
        author varchar(250) NOT NULL,
        rating FLOAT NOT NULL
    )
""")
