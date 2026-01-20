"""Day 59 - Flask Blog (Bootstrap upgrade): main Flask app entrypoint."""

from flask import Flask, render_template

NPOINT_URL = "https://api.npoint.io/35d4767901d354fcdde6"

app = Flask(__name__)


@app.route("/")
def index():
    """
    Docstring for main
    """
    return render_template("index.html")


@app.route("/about")
def about():
    """
    Docstring for about
    """
    return render_template("about.html")


@app.route("/contact")
def contact():
    """
    Docstring for contact
    """
    return render_template("contact.html")


@app.route("/post")
def post():
    """
    Docstring for post
    """
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
