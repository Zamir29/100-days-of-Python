import requests
import datetime
from config import (
    PIXELA_BASE_URL,
    PIXELA_USERNAME,
    PIXELA_TOKEN,
    PIXELA_GRAPH_ID,
    HABIT_NAME,
    HABIT_UNIT,
    HABIT_TYPE,
    HABIT_COLOR,
    PIXELA_GRAPH_URL,
    PIXELA_GRAPH_ID_URL
)

def create_user():
    """Run this once at the beginning"""
    # Find more info on https://docs.pixe.la/entry/post-user#Request-Body
    user_params = {
        "token": PIXELA_TOKEN,
        "username": PIXELA_USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=PIXELA_BASE_URL, json=user_params)

    return response

def create_graph():
    graph_params = {
        "id": PIXELA_GRAPH_ID,
        "name": HABIT_NAME,
        "unit": HABIT_UNIT,
        "type": HABIT_TYPE,
        "color": HABIT_COLOR,
    }

    headers = {
        "X-USER-TOKEN": PIXELA_TOKEN,
    }

    response = requests.post(url=PIXELA_GRAPH_URL, json=graph_params, headers=headers)

    return response

def add_pixel():
    date = datetime.datetime.now().strftime("%Y%m%d")

    pick_date = input("What is the date of the pixel?\n"
                      "[Today] [Another]: ")
    if pick_date.lower() != "today":
        date = input("Give a date with the format yyyyMMdd: ")

    quantity = input(f"What is the quantity in {HABIT_UNIT}?\n"
                          f"Input {HABIT_TYPE}: ")

    pixel_params = {
        "date": date, # yyyyMMdd format
        "quantity": quantity,
    }

    headers = {
        "X-USER-TOKEN": PIXELA_TOKEN,
    }
    response = requests.post(url=PIXELA_GRAPH_ID_URL, json=pixel_params, headers=headers)

    return response