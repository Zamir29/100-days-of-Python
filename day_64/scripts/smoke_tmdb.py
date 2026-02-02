"""
Smoke test for TMDB search.

Goal: verify credentials + endpint + basic response shape without touching Flask routes.
Run as a module to avoid folder position from day_64/ as:
    uv run python -m scripts.smoke_tmdb
"""

import json
from movie_search import SearchMovie

def main_test() -> None:
    """ Use this main to smoke test TMDB """
    query = "Interstellar"

    sm = SearchMovie(query)

    movie_data = sm.search_movie()

    # Basic shape checks
    print(f"type(data): {type(movie_data)}")
    print(f"top_level keys= {list(movie_data.keys())}")

    results = movie_data.get("results", [])
    print(f"results count = {len(results)}")

    #Print just the first result
    first = results[0] if results else None

    if first:
        summary = {
            "id": first.get("id"),
            "title": first.get("title"),
            "release_date": first.get("release_date"),
            "poster_path": first.get("poster_path")
        }
        print("first result summary:")
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    else:
        print("No results returned. Try a different query or check TMDB auth/endpoint.")

if __name__ == "__main__":
    main_test()
