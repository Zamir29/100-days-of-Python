""" Config keeps all the data used in the app"""
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- FLASK WTF ---
WTF_CSRF_SECRET_KEY = os.getenv("WTF_CSRF_SECRET_KEY")
# ---
