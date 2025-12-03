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
    PIXELA_GRAPHS_URL,
)

def create_user():
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

    response = requests.post(url=PIXELA_GRAPHS_URL, json=graph_params, headers=headers)

    return response

def add_pixel():
    date = datetime.datetime.now().strftime("%Y%m%d")

    pick_date = input("What is the date of the pixel?\n"
                      "[Today] [Another]: ")
    if pick_date.lower() != "today":
        date = input("Give a date with the format yyyyMMdd: ")

    quantity = input(f"What is the quantity in {HABIT_UNIT}?\n"
                          f"Input {HABIT_TYPE}: ")

    add_url = f"{PIXELA_GRAPHS_URL}/{PIXELA_GRAPH_ID}"

    pixel_params = {
        "date": date, # yyyyMMdd format
        "quantity": quantity,
    }

    headers = {
        "X-USER-TOKEN": PIXELA_TOKEN,
    }
    response = requests.post(url=add_url, json=pixel_params, headers=headers)

    return response

def update_pixel():
    date = input("What is the pixel's date you want to update?\n"
                 "Please use the format yyyyMMdd: ")
    quantity = input("What is the new quantity?\n"
                     f"Please input {HABIT_TYPE} number: ")

    update_url = f"{PIXELA_GRAPHS_URL}/{PIXELA_GRAPH_ID}/{date}"

    update_params = {
        "quantity": quantity,
    }

    headers = {
        "X-USER-TOKEN": PIXELA_TOKEN,
    }

    response = requests.put(url=update_url, json=update_params, headers=headers)

    return response

def delete_pixel():
    # doc: https://docs.pixe.la/entry/delete-pixel
    date = input("What is the pixel's date you want to delete?\n"
                 "Please use the format yyyyMMdd: ")

    delete_url = f"{PIXELA_GRAPHS_URL}/{PIXELA_GRAPH_ID}/{date}"

    headers = {
        "X-USER-TOKEN": PIXELA_TOKEN,
    }

    response = requests.delete(url=delete_url, headers=headers)

    return response