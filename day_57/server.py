import random
import requests
from datetime import datetime
from flask import Flask, render_template

AGIFY_URL = "https://api.agify.io"
GENDERIZE_URL = "https://api.genderize.io"
NPOINT_URL = "https://api.npoint.io/35d4767901d354fcdde6"

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html",
        random_number=random_number,
        year=year
    )

@app.route('/guess/<string:name>')
def guess(name):
    params = {
        "name": name,
    }
    response_age = requests.get(url=AGIFY_URL, params=params)
    response_age.raise_for_status()
    age = response_age.json().get("age")

    response_gender = requests.get(url=GENDERIZE_URL, params=params)
    response_gender.raise_for_status()
    gender = response_gender.json().get("gender")

    return render_template("guess.html",
                           name=name,
                           gender=gender,
                           age=age,
                           )

@app.route('/blog/<int:num>')
def get_blog(num):
    response_blog = requests.get(url=NPOINT_URL)
    response_blog.raise_for_status()
    all_posts = response_blog.json()

    return render_template("blog.html",
                           all_posts=all_posts,
                           post_num=num,
                           )


if __name__ == '__main__':
    app.run(debug=True)
