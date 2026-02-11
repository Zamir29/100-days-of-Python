"""
This is the Test file for .gitignore and other pieces of Angela's day 70 lessons.
"""
import os
from flask import Flask
from getname import random_name
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_KEY")


@app.route("/")
def hello_world():
    return f"<h1>Behold, I am {random_name('superhero')}!</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
