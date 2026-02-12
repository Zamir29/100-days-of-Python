import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# FLASK APP
SECRET_KEY = os.getenv("SECRET_KEY")
# ---

# SQLALCHEMY APP
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///blog.db")
