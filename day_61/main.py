'''
Red underlines? Install the required packages first:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
from h11 import Data
from config import (
    WTF_CSRF_SECRET_KEY,
)
from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = WTF_CSRF_SECRET_KEY

EMAIL = "admin@testing.test"
PASSWORD = "1234test"
class LoginForm(FlaskForm):
    ''' Login form '''
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()] )
    submit = SubmitField(label='Log in')



@app.route("/")
def home():
    """
    This is home
    """
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    Login page
    """
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == EMAIL and form.password.data == PASSWORD:
            return redirect(url_for("success"))
        else:
            return redirect(url_for("denied"))
        # print(form.email.data)
        # return "Form is valid"
    return render_template("login.html", form=form)

@app.route("/login/success")
def success():
    '''Go to success page in case you made it'''
    return render_template("success.html")

@app.route("/login/denied")
def denied():
    '''Go to denied page in case you failed it'''
    return render_template("denied.html")

if __name__ == '__main__':
    app.run(debug=True)
