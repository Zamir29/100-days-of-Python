'''
Top 10 movies shown in an d-flex html page using Bootstrap framework
'''

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf.csrf import CSRFProtect

from extensions import db
from models import Movie  # pylint: disable=unused-import
from forms import RateMovieForm, AddNewMovie
from config import (
    SECRET_KEY,
    DEV_DB,
)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

Bootstrap5(app)

CSRFProtect(app)

# CREATE DB
db.init_app(app)

# CREATE TABLE


@app.route("/")
def home():
    """ / """
    # Build query with ORM and get the result af all the movies
    stmt = db.select(Movie).order_by(Movie.ranking)
    result = db.session.execute(stmt)
    all_movies = result.scalars().all()

    return render_template("index.html", movies=all_movies)

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    """
    Edit rating and review of a movie.

    Using the ID as the PRIMARY KEY in the URL, the movie is identified

    GET -> show the form prefilled with the current rating and revew
    POST -> update the loaded object with commit
    """

    movie = db.get_or_404(Movie, movie_id)

    form = RateMovieForm()

    if form.validate_on_submit():
        rating = form.rating.data
        review = form.review.data.strip()

        movie.rating = rating
        movie.review = review
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete/<int:movie_id>", methods=["POST"])
def delete_movie(movie_id):
    """
    Delete the movie using the ID as the Primary KEY
    """
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add") #, methods=["POST"])
def add_movie():
    """ Uses a form to retrive a title to add to the databse """
    add_new_movie = AddNewMovie()

    if add_new_movie.validate_on_submit():
        movie_title = add_new_movie.movie_title.data.strip()

        


    return render_template("add.html", add_movie=add_new_movie)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
