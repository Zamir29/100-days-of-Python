import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

PIXELA_BASE_URL = "https://pixe.la/v1/users"

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")

HABIT_NAME = ""
HABIT_UNIT = ""
HABIT_TYPE = ""
HABIT_COLOR = "" # shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black)