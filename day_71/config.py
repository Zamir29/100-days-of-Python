import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# FLASK APP
SECRET_KEY = os.getenv("SECRET_KEY")
# ---

# SQLALCHEMY APP
DB_URI = os.getenv("DATABASE_URL")
