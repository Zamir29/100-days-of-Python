import requests
from config import NPOINT_URL


class Post:
    def __init__(self):
        response_blog = requests.get(url=NPOINT_URL, timeout=5)
        response_blog.raise_for_status()

        posts = response_blog.json()

        # Normalize in case npoint returns {"posts": [...]} instead of a list.
        if isinstance(posts, dict) and "posts" in posts:
            posts = posts["posts"]

        self._posts: list[dict] = posts
        self._by_id: dict[int, dict] = {post["id"]: post for post in self._posts}

    def all_posts(self) -> list[dict]:
        return self._posts

    def by_id(self, post_id: int) -> dict | None:
        return self._by_id.get(post_id)

    def refresh(self) -> None:
        response_blog = requests.get(url=NPOINT_URL, timeout=5)
        response_blog.raise_for_status()

        posts = response_blog.json()
        if isinstance(posts, dict) and "posts" in posts:
            posts = posts["posts"]

        self._posts = posts
        self._by_id = {post["id"]: post for post in self._posts}