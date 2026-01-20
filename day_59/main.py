"""Day 59 - Flask Blog (Bootstrap upgrade): main Flask app entrypoint."""

from flask import Flask, render_template, abort
from posts import PostRepository

app = Flask(__name__)

# Initialize the repository
post_repo = PostRepository()


@app.route("/")
def index():
    """
    Docstring for main
    """
    all_posts = post_repo.all_posts()
    return render_template("index.html", all_posts=all_posts)


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


@app.route("/post/<int:post_id>")
def post(post_id):
    """
    Docstring for post
    """
    post_data = post_repo.by_id(post_id)
    if post_data is None:
        abort(404)
    return render_template("post.html", post_data=post_data)


if __name__ == "__main__":
    app.run(debug=True)
