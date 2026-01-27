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


app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    """ Home of the Virtual Bookshelf """
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    """ Form to add a new book """
    if request.method == "POST":
        new_book = {
            "title": request.form["title"].strip(),
            "author": request.form["author"].strip(),
            "rating": request.form["rating"].strip(),
        }
        all_books.append(new_book)
        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
