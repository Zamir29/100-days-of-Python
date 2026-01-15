from flask import Flask, render_template, abort
from post import Post

app = Flask(__name__)

# Create the posts service/repository once at startup
posts = Post()


@app.route("/")
def home():
    return render_template(
        "index.html",
        all_posts=posts.all_posts(),
    )


@app.route("/post/<int:post_id>")
def show_post(post_id: int):
    post_content = posts.by_id(post_id)

    if post_content is None:
        abort(404)

    return render_template(
        "post.html",
        post_content=post_content,
    )


if __name__ == "__main__":
    app.run(debug=True)