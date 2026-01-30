'''
Top 10 movies shown in an d-flex html page using Bootstrap framework
'''

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, InputRequired

from extensions import db
from models import Movie  # pylint: disable=unused-import
from config import (
    SECRET_KEY,
    DEV_DB,
)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

Bootstrap5(app)

# CREATE DB
db.init_app(app)

# CREATE TABLE
class RateMovieForm(FlaskForm):
    """ WTForm used to edit the movie's rating and review """
    rating = FloatField("Your Rating out of 10 e.g. 7.5", validators=[InputRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

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


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
