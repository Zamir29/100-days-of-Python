'''
Top 10 movies shown in an d-flex html page using Bootstrap framework
'''

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5

# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired

from extensions import db
from models import Movie  # pylint: disable=unused-import
from config import (
    SECRET_KEY,
    DEV_DB,
)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

Bootstrap5(app)

# CREATE DB
db.init_app(app)

# CREATE TABLE


@app.route("/")
def home():
    """ / """
    return render_template("index.html")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
