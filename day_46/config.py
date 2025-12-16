import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- WIKIPEDIA Billboard Year-end 100 singles list ---

BILLBOARD_LISTS_URL = "https://en.wikipedia.org/wiki/Category%3ALists_of_Billboard_Year-End_Hot_100_singles"
BILLBOARD_URL = "https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_"