"""
Smoke testing for the database
Run as a module to avoid folder position from day_64/ as:
    uv run python -m scripts.smoke_db
"""

import main
from extensions import db
from models import Movie

# main.app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB

test_movies = [
    {
      "title": "Avatar - The way of water",
      "year": 2022,
      "description": "Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
      "rating": 7.3,
      "ranking": 9,
      "review": "I liked the water",
      "img_url": "https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg",
    },
    {
      "title": "Interstellar",
      "year": 2014,
      "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
      "rating": 9.3,
      "ranking": 1,
      "review": "A masterpiece — the docking scene is unreal.",
      "img_url": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
    },
    {
      "title": "Inception",
      "year": 2010,
      "description": "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
      "rating": 8.9,
      "ranking": 3,
      "review": "Still the cleanest mind-bender. That ending…",
      "img_url": "https://image.tmdb.org/t/p/w500/edv5CZvWj09upOsy2Y6IwDhK8bt.jpg",
    },
]

def get_by_title(title):
    """ Helper to verify if the movie is already present in the database """
    stmt = db.select(Movie).where(Movie.title == title)
    result = db.session.execute(stmt)
    movie = result.scalars().one_or_none()
    return movie

def seed_movie(movie):
    """ idempotent helper that seed a movie if it is not present yet """
    movie_title = movie["title"]
    if get_by_title(movie_title):
        print(f"🤔 The movie '{movie_title}' appears to be already present in the database")
        return

    new_movie = Movie(
        title=movie_title,
        year=movie["year"],
        description=movie["description"],
        rating=movie["rating"],
        ranking=movie["ranking"],
        review=movie["review"],
        img_url=movie["img_url"],
    )
    db.session.add(new_movie)
    db.session.commit()
    print(f"✅ Added the movie '{movie_title}'!!!")

def main_test():
    """ This function mimics the main for test purpose"""
    with main.app.app_context():
        db.create_all()
        for movie in test_movies:
            seed_movie(movie=movie)
        print("Schema ensured")


if __name__ == "__main__":
    main_test()
