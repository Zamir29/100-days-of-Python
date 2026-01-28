import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- SQL DATABASE
DEV_DB = "sqlite:///instance/movies_dev.db"
TEST_DB = "sqlite:///instance/movies_test.db"
# ---
