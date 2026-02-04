'''
Make sure the required packages are installed:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['CKEDITOR_PKG_TYPE'] = "standard"
ckeditor = CKEditor(app)
Bootstrap5(app)



# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CONFIGURE POST FORM
class PostForm(FlaskForm):
    title = StringField("Post title", validators=[DataRequired(), ])
    subtitle = StringField("Post subtitle", validators=[DataRequired()])
    author = StringField("Author name", validators=[DataRequired()])
    img_url = StringField("Background URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Body text", validators=[DataRequired()])
    submit = SubmitField("Publish")

# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    post_db = db.select(BlogPost)
    result = db.session.execute(post_db)
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/create_post", methods=["GET", "POST"])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = BlogPost()

        for column in new_post.__table__.columns:

            if column.name == "id":
                continue

            if column.name == "date":
                get_time = datetime.now()
                new_post.date = get_time.strftime("%B %d, %Y")
            else:
                value = form[column.name].data
                setattr(new_post, column.name, value)

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form)
# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post_data = db.get_or_404(BlogPost, post_id)
    form = PostForm()

    if request.method == "GET":
        for field in form:
            if field.name not in ("submit", "csrf_token"):
                field.data = getattr(post_data, field.name)

    if form.validate_on_submit():
        for column in post_data.__table__.columns:

            if column.name == "id":
                continue

            if column.name == "date":
                # Date must not change based on Angela's requiremnts
                continue

            value = form[column.name].data
            setattr(post_data, column.name, value)

        db.session.commit()

        return redirect(url_for("show_post", post_id=post_id))

    return render_template("make-post.html", edit_mode=True, form=form)

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete-post/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    post_data = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_data)
    db.session.commit()

    return redirect(url_for("get_all_posts"))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
