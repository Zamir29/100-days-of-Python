'''
Red underlines? Install the required packages first:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


# SQLAlchemy setup
class Base(DeclarativeBase):
    """ Use the class Base to pass DeclarativeBase to the constructor """
    pass
db = SQLAlchemy(model_class=Base)

# Create the app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

# Attach SQLAlchemy to Flask
db.init_app(app)

class Book(db.Model):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

@app.route('/')
def home():
    """ Home of the Virtual Bookshelf """
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    """ Form to add a new book """
    if request.method == "POST":
        title= request.form["title"].strip()
        author = request.form["author"].strip()
        rating_raw = request.form["rating"].strip()

        # Minimal input hygiene
        if not title or not author or not rating_raw:
            return render_template("add.html")

        new_book = Book(
            title=title,
            author=author,
            rating=float(rating_raw),
        )

        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html")

with app.app_context():
    db.create_all()
    
if __name__ == "__main__":
    app.run(debug=True)
