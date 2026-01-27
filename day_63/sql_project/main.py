"""Day 63 — SQLite intro.

Goal: Create a local SQLite database file and a simple `books` table.
Note: This script is safe to re-run (uses IF NOT EXISTS).
"""

import sqlite3

DB_PATH = "books-collection.db"

def main() -> None:
    """ Main function to run the script """
    # `with` ensures the connection is properly closed even if an error happens
    with sqlite3.connect(DB_PATH) as db:
        cursor = db.cursor()

        cursor.execute("""
            CREATE TABLE books (
                id INTEGER PRIMARY KEY,
                title varchar(250) NOT NULL UNIQUE,
                author varchar(250) NOT NULL,
                rating FLOAT NOT NULL
            )
            """
        )
        db.commit()

if __name__ == "__main__":
    main()
