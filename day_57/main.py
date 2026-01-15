import requests
from flask import Flask, render_template, abort

NPOINT_URL = "https://api.npoint.io/35d4767901d354fcdde6"

response_blog = requests.get(url=NPOINT_URL)
response_blog.raise_for_status()
all_posts = response_blog.json()

# Build an index for fast lookups: {id: post_dict}
post_by_id = {post["id"]: post for post in all_posts}

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html",
                           all_posts=all_posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post_content = post_by_id[post_id]
    if post_content is None:
        abort(404)

    return render_template("post.html",
                           post_content=post_content,
                           )

if __name__ == "__main__":
    app.run(debug=True)
