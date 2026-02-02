import requests
from config import (
    TMBD_READ_TOKEN,
    TMDB_API_KEY,
    TMDB_ENDPOINT,
)

class SearchMovie():
    def __init__(self, movie_title) -> None:
        self.movie_title = movie_title
        self.tmdb_key = TMDB_API_KEY
        self.tmdb_read_token = TMBD_READ_TOKEN
        self.tmdb_endpoint = TMDB_ENDPOINT


    def search_movie(self):
        headers = {
            "Authorization": f"Bearer {self.tmdb_read_token}",
            "accept": "application/json"
        }

        params = {
            "query": self.movie_title,
        }

        response = requests.get(url=self.tmdb_endpoint,headers=headers, params=params, timeout=20)
        response.raise_for_status()

        print("endpoint:", self.tmdb_endpoint)
        print("status:", response.status_code)
        print("final url:", response.url)
        print("payload preview:", response.text[:200])
        
        return response.json()
