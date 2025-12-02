import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")