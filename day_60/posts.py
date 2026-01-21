"""posts.py
Day 59 - Simple blog post loader.
Goal:
- `Post` = a tiny object that holds data like `title`, `date`, etc.
- `PostRepository` = fetches posts from NPOINT_URL and lets you:
    - get all posts
    - get one post by id

This keeps your Flask routes/templates clean:
- routes call repo.all_posts() / repo.by_id(id)
- templates use post.title, post.date, ...
"""

import requests
from config import NPOINT_URL


class Post:
    """A blog post with fields like title, subtitle, body, date, author, image."""

    def __init__(self, data):
        # `data` is a dict coming from JSON.
        # We store the fields we care about as attributes.
        if data is None:
            data = {}

        raw_id = data.get("id")
        if isinstance(raw_id, int):
            self.id = raw_id
        elif isinstance(raw_id, str):
            self.id = int(raw_id) if raw_id.isdigit() else None
        else:
            self.id = None

        self.title = data.get("title", "")
        self.subtitle = data.get("subtitle", "")
        self.body = data.get("body", "")
        self.date = data.get("date", "")
        self.author = data.get("author", "")
        self.image = data.get(
            "image", ""
        )  # e.g. "assets/img/home-bg.jpg" inside /static


class PostRepository:
    """Fetches and caches posts from the remote JSON endpoint."""

    def __init__(self, url=NPOINT_URL, timeout=5):
        self.url = url
        self.timeout = timeout

        # Cache:
        self._posts = []  # list of Post objects
        self._by_id = {}  # dict: id -> Post

        # Load data once at startup
        self.refresh()

    def _fetch_raw_posts(self):
        """Return a list of raw dict posts from the endpoint."""
        response = requests.get(self.url, timeout=self.timeout)
        response.raise_for_status()

        data = response.json()

        # Some endpoints return a list directly:
        #   [ {...}, {...} ]
        # Others return a dict with a 'posts' key:
        #   {"posts": [ {...}, {...} ]}
        if isinstance(data, dict) and "posts" in data:
            data = data["posts"]

        if not isinstance(data, list):
            raise ValueError(
                "Unexpected JSON shape: expected a list or {'posts': [...]}."
            )

        return data

    def refresh(self):
        """Re-fetch posts and rebuild the cache."""
        raw_posts = self._fetch_raw_posts()

        posts = []
        by_id = {}

        for item in raw_posts:
            post = Post(item)
            posts.append(post)

            # Only index posts that have an id
            if post.id is not None:
                by_id[post.id] = post

        # Cache for fast access
        self._posts = posts
        self._by_id = by_id

    def all_posts(self):
        """Return all cached posts (list of Post objects)."""
        return self._posts

    def by_id(self, post_id):
        """Return a single post by id, or None if not found."""
        return self._by_id.get(post_id)
