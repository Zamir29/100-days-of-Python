"""
Smoke test for TMDB search.

Goal: verify credentials + endpint + basic response shape without touching Flask routes.
Run as a module to avoid folder position from day_64/ as:
    uv run python -m scripts.smoke_tmdb
"""

import json
from movie_search import TMDBApi

def main_test() -> None:
    """ Use this main to smoke test TMDB """
    query = "Interstellar"

    sm = TMDBApi()

    movie_response = sm.get_response(query)

    # Movie response
    print("endpoint:", sm.tmdb_endpoint)
    print("status:", movie_response.status_code)
    print("final url:", movie_response.url)
    print("payload preview:", movie_response.text[:200])

    # Basic shape checks
    movie_data = sm.search_movie(movie_title=query)
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
        image_path = sm.movie_image_path(file_path=summary["poster_path"], width="500")

        print("first result summary:")
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        print(image_path)
    else:
        print("No results returned. Try a different query or check TMDB auth/endpoint.")

if __name__ == "__main__":
    main_test()
