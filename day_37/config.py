import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

PIXELA_BASE_URL = "https://pixe.la/v1/users"

# Retrieve fron .env
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")

# Graph builder
VISIT_PAGE = "https://pixe.la/@zamirhashorva"
PIXELA_GRAPHS_URL = f"{PIXELA_BASE_URL}/{PIXELA_USERNAME}/graphs"

# Graph with id: graph001
PIXELA_GRAPH_ID= "graph001"
HABIT_NAME = "Coding"
HABIT_UNIT = "min"
HABIT_TYPE = "int"
HABIT_COLOR = "shibafu" # shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black)
