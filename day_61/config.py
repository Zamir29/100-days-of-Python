"""Config keeps all the data used in the app"""

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# --- FLASK WTF ---
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
# ---
