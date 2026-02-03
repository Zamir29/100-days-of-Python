"""
Using The Movie Database to retrive data for movies starting from a movie title query
link: https://developer.themoviedb.org/docs/search-and-query-for-details

The image url needs three parts:
`base_url`, a `file_size` and a `file_path`.
Image base url is in `config.py`, while the file size is in the class attributes
"""
import requests
from requests import Response
from config import (
    TMDB_READ_TOKEN,
    TMDB_URL,
    TMDB_URL_IMAGE
)

class TMDBApi:
    """ Class to manage the operation on the TMDB API """
    def __init__(
        self,
        read_token: str | None = TMDB_READ_TOKEN,
        base_url: str = TMDB_URL,
        image_base_url: str = TMDB_URL_IMAGE,
        timeout_s: int = 20,
    ) -> None:
        self.read_token = read_token
        self.base_url = base_url.rstrip("/")
        self.endpoint = f"{self.base_url}/search/movie"
        self.endpoint_id = f"{self.base_url}/movie/"
        self.image_base_url = image_base_url.rstrip("/")
        self.timeout_s = timeout_s

        #Supported image sizes (TMDB)
        self.image_size = {
            "full": "/original",
            "1280": "/w1280",
            "780": "/w780",
            "500": "/w500",
        }
    def headers(self):
        """Create the headers correctly for any API call at TMDB

        Raises:
            ValueError: Never miss to add the token from config

        Returns:
            _type_: a dict of paramaters for request
        """
        if not self.read_token:
            raise ValueError("Missing TMDB read token. Set TMDB_READ_TOKEN in your environment.")

        return {
            "Authorization": f"Bearer {self.read_token}",
            "accept": "application/json",
        }

    def get_response(self, query: str) -> Response:
        """
        Perform the TMDB search/movie request and return the raw Response.

        Raises:
            requests.HTTPError: on non-2xx responses.
        """

        params = {
            "query": query,
        }

        response = requests.get(
            url=self.endpoint,
            headers=self.headers(),
            params=params,
            timeout=self.timeout_s
        )

        # Fail fast on 401/404/500 etc.
        response.raise_for_status()

        return response

    def parse_json(self, response: Response):
        """Parse a Response to a dict. Raises friendly error if not JSON.

        Args:
            response (Response): the object is a Response
        """
        try:
            data = response.json()
        except ValueError as e:
            raise ValueError("TMDB response was not valid JSON") from e

        if not isinstance(data, dict):
            raise TypeError(f"Expected JSON object (dict), got {type(data)}.")

        return data

    def search_movie(self, query: str):
        """
        Search and return the full JSON dict.
        """
        resp = self.get_response(query)
        return self.parse_json(resp)

    def search_results(self, query: str):
        """
        Return only the list of results.
        """
        data = self.search_movie(query)
        results = data.get("results", [])
        if not isinstance(results, list):
            raise TypeError("TMDB 'results' field was not a list")
        return results

    def get_details_response(self, tmdb_id: int) -> Response:
        """Response for the url with movie ID

        Args:
            tmdb_id (int): ID of the movie

        Returns:
            _type_: Response
        """
        url_id = f"{self.endpoint_id}{tmdb_id}"
        response = requests.get(
            url=url_id,
            headers=self.headers(),
            timeout=self.timeout_s
        )
        response.raise_for_status()
        return response

    def movie_id_details(self, tmdb_id: int):
        """Get details of a movie from the ID

        Args:
            tmdb_id (int): id found in search results

        Returns:
            _type_: a dictionary of data belonging to the movie
        """
        response = self.get_details_response(tmdb_id=tmdb_id)
        return self.parse_json(response=response)


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
                size_part = self.image_size[width]
                return f"{self.image_base_url}{size_part}{file_path}"

        return "https://placehold.co/1000x1000?text=No+Image"
