"""Day 59 - Flask Blog (Bootstrap upgrade): main Flask app entrypoint."""

from flask import Flask, redirect, render_template, abort, request, url_for
from posts import PostRepository
from config import (
    GMAIL_SMTP,
    ZCH_MAIL,
    MY_EMAIL,
    MY_PASSWORD,
)

app = Flask(__name__)

# Initialize the repository
post_repo = PostRepository()


@app.route("/")
def index():
    """Render the homepage with the list of blog posts."""
    all_posts = post_repo.all_posts()
    return render_template("index.html", all_posts=all_posts)


@app.route("/about")
def about():
    """Serve the About page template."""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Serve the Contact page template."""
    return render_template("contact.html")

@app.route("/contact/submit", methods=["POST"])
def contact_submit():
    """Submit data from the Contact page template."""
    name = (request.form.get("name") or "").strip()
    email = (request.form.get("email") or "").strip()
    phone = (request.form.get("phone") or "").strip()
    message = (request.form.get("message") or "").strip()

    # If any field is missing, redirect to back to contact with error status
    if not name or not email or not message:
        return redirect(url_for("contact", status="error"))
    elif "@" not in email:
        return redirect(url_for("contact", status="error"))
    else:
        return redirect(url_for("contact", status="success"))


@app.route("/post/<int:post_id>")
def post(post_id):
    """Serve the post detail page for the given post_id or 404 if missing."""
    post_data = post_repo.by_id(post_id)
    if post_data is None:
        abort(404)
    return render_template("post.html", post_data=post_data)


if __name__ == "__main__":
    app.run(debug=True)
