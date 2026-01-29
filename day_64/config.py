""" config file for Top 10 movies webapp """
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- SQL DATABASE
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)

DEV_DB = f"sqlite:///{os.path.join(INSTANCE_DIR, 'movies_dev.db')}"
TEST_DB = f"sqlite:///{os.path.join(INSTANCE_DIR, 'movies_test.db')}"
# ---

# --- FLASK WTFORM SECRET KEY ---
SECRET_KEY = os.getenv("SECRET_KEY", "dev-not-secret")
# ---
