""" Set of forms used in the webapp """

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, InputRequired

class RateMovieForm(FlaskForm):
    """ WTForm used to edit the movie's rating and review """
    rating = FloatField("Your Rating out of 10 e.g. 7.5", validators=[InputRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

class AddNewMovie(FlaskForm):
    """ WTForm used to fetch the title of a new movie to add to the database """
    movie_title = StringField("Movie title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")
