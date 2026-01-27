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
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title varchar(250) NOT NULL UNIQUE,
                author varchar(250) NOT NULL,
                rating FLOAT NOT NULL
            )
            """
        )
        cursor.execute(
            """
            INSERT OR IGNORE INTO books (id, title, author, rating)
            VALUES(
                1,
                'Harry Potter',
                'J. K. Rowling',
                '9.3'
            )
            """
        )

        db.commit()

if __name__ == "__main__":
    main()
