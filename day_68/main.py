"""Day 68 Authentication with Flask"""

from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key-goes-here"
app.config["UPLOAD_FOLDER"] = "static/files"


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(200))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()

# CREATE LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id: str):
    try:
        return db.session.get(User, int(user_id))
    except (TypeError, ValueError):
        return None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        password_in = request.form.get("password")
        if password_in is None:
            return redirect(url_for("register"))

        # Hashing and salting the password entered by the user
        password_out = generate_password_hash(
            password=password_in, method="pbkdf2:sha256", salt_length=8
        )
        new_user = User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            password=password_out,
        )

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        flash("Welcome in the secrets")

        return redirect(url_for("secrets"))

    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password_in = request.form.get("password")
        if password_in is None:
            return redirect(url_for("login"))

        email_in = request.form.get("email")

        user = db.one_or_404(db.select(User).filter_by(email=email_in))
        if check_password_hash(pwhash=user.password, password=password_in):

            login_user(user)
            flash("Logged in succesfully")

            return redirect(url_for("secrets"))

    return render_template("login.html")


@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():

    return send_from_directory(
        directory=app.config["UPLOAD_FOLDER"],
        path="cheat_sheet.pdf",
        as_attachment=True,
    )


if __name__ == "__main__":
    app.run(debug=True)
