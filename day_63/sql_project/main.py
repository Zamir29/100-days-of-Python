"""Day 63 — SQLAlchemy + SQLite intro.

Requirements:
- Create an SQLite database called `new-books-collection.db`.
- Create a `books` table with: id, title, author, rating.
- Apply the same constraints as the raw SQL version (NOT NULL, UNIQUE, etc.).
- With a Flask app context, create the schema and add one starter row.

Note: This script is safe to re-run (it won't duplicate the starter row).
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# --- SQLAlchemy setup
class Base(DeclarativeBase):
    """ Use the clase Base to pass DeclarativeBase to the constructor """

db = SQLAlchemy(model_class=Base)

# Create the app

# --- Flask app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Attach SQLAlchemy to Flask
db.init_app(app)

class Book(db.Model):
    """ Books table schema. """
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


def main() -> None:
    """ Create tables and insert the starter book (id=1) once. """
    with app.app_context():
        db.create_all()

    # Seed row required by Angela's challenge
    # Making it idempotent (safe to re-run).
        existing = db.session.get(Book, 1)
        if existing is None:
            starter = Book( # type: ignore[call-arg]
                id=1,
                title="Harry Potter",
                author="J. K. Rowling",
                rating=9.3,
            )
            db.session.add(starter)
            db.session.commit()

if __name__ == "__main__":
    main()
