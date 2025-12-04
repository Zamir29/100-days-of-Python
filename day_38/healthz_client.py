import requests
from config import (
    X_APP_KEY,
    X_APP_ID,
    X_APP_URL,
    X_APP_GET,
    X_APP_POST,
    ERROR_CODE,
)

def get_exercise_stats():
    get_query = input("Tell me which exercise you did: ")

    query_params = {
        "query": get_query,
    }

    headers = {
        "x-app-id": X_APP_ID,
        "x-app-key": X_APP_KEY,
    }

    response = requests.post(url=X_APP_POST, json=query_params, headers=headers)

    return response