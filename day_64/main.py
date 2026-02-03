"""
Top 10 movies shown in an d-flex html page using Bootstrap framework
"""

from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf.csrf import CSRFProtect

from extensions import db
from models import Movie  # pylint: disable=unused-import
from forms import RateMovieForm, AddNewMovie
from movie_search import TMDBApi
from config import (
    SECRET_KEY,
    DEV_DB,
)

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DEV_DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

Bootstrap5(app)

CSRFProtect(app)

# CREATE DB
db.init_app(app)

# CREATE TABLE


@app.route("/")
def home():
    """/"""
    # Build query with ORM and get the result af all the movies
    stmt = db.select(Movie).order_by(Movie.ranking.is_(None), Movie.rating.desc())
    result = db.session.execute(stmt)
    all_movies = result.scalars().all()
    movies_ranked = [(i, movie) for i, movie in enumerate(all_movies, start=1)]

    return render_template("index.html", movies=movies_ranked)


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
        review = (form.review.data or "").strip()

        movie.rating = float(rating) if rating is not None else 0.0
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


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    """Uses a form to retrive a title to add to the databse"""
    add_new_movie = AddNewMovie()

    if add_new_movie.validate_on_submit():
        movie_title = ((add_new_movie.movie_title.data or "").strip() or "Untitled")

        return redirect(url_for("select_movie", query=movie_title))

    return render_template("add.html", add_movie=add_new_movie)


@app.route("/select", methods=["GET"])
def select_movie():
    """Renders a list of movies as a result from the query

    Returns:
        _type_: id of the movie
    """
    query = request.args.get("query")
    if not query:
        return redirect(url_for("add_movie"))

    tmdb = TMDBApi()
    movies = tmdb.search_results(query)
    for movie in movies:
        poster_path = movie.get("poster_path")
        movie["poster_url"] = tmdb.movie_image_path(poster_path)
    return render_template("select.html", movies=movies)


@app.route("/find/<int:tmdb_id>", methods=["GET"])
def find_movie(tmdb_id):
    """ Find movie will use the id in select.html to retrive the data for a specific movie

    Args:
        tmdb_id (int): the id from the movie database

    Returns:
        url: edit.html to add the review and rating from the user
    """
    tmdb = TMDBApi()
    # Fetch full details for the selected TMDB id
    movie_details = tmdb.movie_id_details(tmdb_id=tmdb_id)

    poster_path = movie_details.get("poster_path")
    img_url = tmdb.movie_image_path(file_path=poster_path, width="full")

    release_date = movie_details.get("release_date", None)
    year = int(release_date[:4]) if release_date else None

    title = movie_details.get("title") or movie_details.get("original_title") or "Untitled"

    description = movie_details.get("overview") or ""

    movie_data = Movie(
        title= title,  # type: ignore[reportCallIssue]
        year= year, # type: ignore[reportCallIssue]
        description= description,  # type: ignore[reportCallIssue]
        rating= 0.0, # type: ignore[reportCallIssue]
        ranking= 9999, # type: ignore[reportCallIssue]
        review= "", # type: ignore[reportCallIssue]
        img_url= img_url, # type: ignore[reportCallIssue]
    )

    db.session.add(movie_data)
    db.session.commit()


    return redirect(url_for("edit", movie_id=movie_data.id))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
