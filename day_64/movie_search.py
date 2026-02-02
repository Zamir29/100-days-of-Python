"""
Using The Movie Database to retrive data for movies starting from a movie title query
link: https://developer.themoviedb.org/docs/search-and-query-for-details

The image url needs three parts:
`base_url`, a `file_size` and a `file_path`.
Image base url is in `config.py`, while the file size is in the class attributes
"""
import requests
from config import (
    TMBD_READ_TOKEN,
    TMDB_API_KEY,
    TMDB_ENDPOINT,
    TMDB_URL_IMAGE
)

class TMDBApi():
    def __init__(self) -> None:
        self.tmdb_key = TMDB_API_KEY
        self.tmdb_read_token = TMBD_READ_TOKEN
        self.tmdb_endpoint = TMDB_ENDPOINT
        self.tmdb_url_image = TMDB_URL_IMAGE
        self.image_size = {
            "full": "/original",
            "1280": "/w1280",
            "780": "/w780",
            "500": "/w500",
        }

    def get_response(self, movie_title: str = "Interstellar"):
        headers = {
            "Authorization": f"Bearer {self.tmdb_read_token}",
            "accept": "application/json"
        }

        params = {
            "query": movie_title,
        }

        response = requests.get(url=self.tmdb_endpoint,headers=headers, params=params, timeout=20)
        response.raise_for_status()

        return response

    def search_movie(self, movie_title: str):
        return self.get_response(movie_title=movie_title).json()

    def movie_image_path(self, file_path, width: str = "500"):
        """This helper build the image path from the search_movie data

        Args:
            file_path (str): this path is part of the search_movie outcome
            width (str): a keyword that is part of the list in the class attributes

        Returns:
            str: composed url of the three required parts
        """
        if file_path:
            width = str(width)
            if width in self.image_size:
                movie_image = self.image_size[width]
                return f"{self.tmdb_url_image}{movie_image}{file_path}"

        return "https://placehold.co/1000x1000?text=No+Image"
