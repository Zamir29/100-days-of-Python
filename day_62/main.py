"""
Red underlines? Install the required packages first:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""

import csv
from pathlib import Path
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

# Keep the CSV path stable even when run the app from a different working directory
CSV_FILE = Path(__file__).with_name("cafe-data.csv")


class CafeForm(FlaskForm):
    """ WTForm used to add a new cafe. """

    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField(
        "Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()]
    )
    open_time = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close_time = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField(
        "Coffee Rating",
        choices=[
            ("0", "✘"),
            ("1", "☕️"),
            ("2", "☕️☕️"),
            ("3", "☕️☕️☕️"),
            ("4", "☕️☕️☕️☕️"),
            ("5", "☕️☕️☕️☕️☕️"),
        ],
        validators=[DataRequired()],
    )
    wifi_rating = SelectField(
        "Wifi Strength Rating",
        choices=[
            ("0", "✘"),
            ("1", "💪"),
            ("2", "💪💪"),
            ("3", "💪💪💪"),
            ("4", "💪💪💪💪"),
            ("5", "💪💪💪💪💪"),

        ],
        validators=[DataRequired()],
    )
    power_rating = SelectField(
        "Power Socket Availability",
        choices=[
            ("0", "✘"),
            ("1", "🔌"),
            ("2", "🔌🔌"),
            ("3", "🔌🔌🔌"),
            ("4", "🔌🔌🔌🔌"),
            ("5", "🔌🔌🔌🔌🔌"),
        ],
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")


@app.route("/")
def home():
    """
    Home of cafe
    """
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    """
    Hidden route to add details for a new cafe
    """
    form = CafeForm()
    if form.validate_on_submit():
        assert form.cafe.data is not None
        assert form.location.data is not None
        assert form.open_time.data is not None
        assert form.close_time.data is not None

        with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(
                [
                    form.cafe.data.strip(),
                    form.location.data.strip(),
                    form.open_time.data.strip(),
                    form.close_time.data.strip(),
                    form.coffee_rating.data,
                    form.wifi_rating.data,
                    form.power_rating.data,
                ]
            )
        return redirect(url_for("cafes"))
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    """
    List of all cafes submitted
    """
    with open(CSV_FILE, newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
