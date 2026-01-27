"""
Day 63 — SQLAlchemy + Flask CRUD (Add + Edit)

This file is intentionally small and "course-aligned" (Angela Yu), but the comments explain the real
mechanics so future-you remembers *why* each piece exists.

Key ideas:
- Flask runs request handlers (routes). During a request,
  Flask automatically provides an app+request context.
- Flask-SQLAlchemy needs an *active app context* to know
  which app/config (DB URI) is currently in use.
- SQLAlchemy ORM maps a Python class (Book) to a DB table (books). Instances of Book represent rows.
- `db.session` is the "unit of work": stage changes (add/update/delete) and `commit()` to persist.

CLI tip to inspect data:
- `sqlite3 instance/books-collection.db` (or the path shown in your project)
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# SQLAlchemy = the database toolkit/ORM.
# Flask-SQLAlchemy = a thin integration layer that wires SQLAlchemy into Flask's app/context lifecycle.


# SQLAlchemy setup
class Base(DeclarativeBase):
    """
    Declarative base class used by SQLAlchemy 2.0 style mappings.

    Flask-SQLAlchemy 3.1+ expects a DeclarativeBase subclass when you pass `model_class=...`.
    Think of this as: "all my ORM models hang off this base".
    """
    pass


# `db` is the Flask-SQLAlchemy extension object. It will later be bound to the Flask app via `init_app()`.
db = SQLAlchemy(model_class=Base)

# Create the Flask app object (this holds config and routes).
app = Flask(__name__)

# Database URL. For SQLite, `sqlite:///file.db` is a relative path.
# Flask may place the SQLite file under the app's `instance/` folder (runtime data, usually gitignored).
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

# Bind the SQLAlchemy extension to this Flask app.
# After this, inside a request (or inside `app.app_context()`), you can use `db.session`.
db.init_app(app)

# ORM Model = Table definition
# - `Book` maps to the `books` table.
# - Each `Book(...)` instance is a row.
# - `Mapped[...]` + `mapped_column(...)` is the SQLAlchemy 2.0 typed ORM style.

class Book(db.Model):
    """
    The class defines the schema for the table and refers to the columns required for a Book
    """

    # Explicit table name (otherwise SQLAlchemy would derive it from the class name).
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


@app.route("/")
def home():
    """
    List all books.

    Important: routes run inside Flask's automatic request context.
    That means we can use `db.session` here without manually pushing `app.app_context()`.
    """
    # SQLAlchemy 2.0 style SELECT. `execute()` returns a Result, then `scalars()` gives Book objects.
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    """
    Add a new book.

    GET  -> show the form.
    POST -> validate inputs, create a Book object, add to session, commit to persist.
    """
    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        rating_raw = request.form["rating"].strip()

        # Minimal input hygiene
        if not title or not author or not rating_raw:
            return render_template("add.html")

        # Build a Python object (not yet saved). It becomes a DB row only after `commit()`.
        new_book = Book(
            title=title,
            author=author,
            rating=float(rating_raw),
        )
        # Stage the insert in the current transaction.
        db.session.add(new_book)

        # Commit = make it permanent in the database.
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    """Edit the rating of an existing book.

    We identify the record by PRIMARY KEY (id) in the URL.
    GET  -> show the form prefilled with the current rating.
    POST -> update the loaded object and commit.
    """
    # Load the Book row (or return a 404 page if the id doesn't exist).

    book = db.get_or_404(Book, book_id)

    if request.method == "POST":
        rating_raw = request.form["rating"].strip()

        # Update the in-memory object; commit will persist the change.
        book.rating = float(rating_raw)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", book=book)

# Create tables once at startup.
# This code runs OUTSIDE a request, so Flask will NOT auto-create a context.
# We manually push an app context so Flask-SQLAlchemy knows which app/config to use.
with app.app_context():
    db.create_all()

# Run the development server (debug=True enables auto-reload and better error pages).
if __name__ == "__main__":
    app.run(debug=True)
