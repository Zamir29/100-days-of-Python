"""Day 60 - Flask Blog (Bootstrap upgrade): Add Contact form submit."""

from email.message import EmailMessage
import smtplib
import sqlite3
from datetime import datetime, timezone
from flask import Flask, redirect, render_template, abort, request, url_for
from posts import PostRepository
from config import (
    GMAIL_SMTP,
    ZCH_MAIL,
    MY_EMAIL,
    MY_PASSWORD,
    DATA_DIR,
    DB_PATH,
)


# SQLite helper for Day 60 Upgrade (not required by the course)
def init_db() -> None:
    """Create the SQLite DB folder + table if they don't exist yet."""
    # Ensure directory /data exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    with sqlite3.connect(DB_PATH) as conn:
        # Execute a command idempotent in case db doesn't exists
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS contact_submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at_utc TEXT NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                message TEXT NOT NULL,
                ip TEXT,
                user_agent TEXT
            )
        """
        )
        # Commit changes to db
        conn.commit()


# Save submission on the DB contact_submission, returns a submission_id
def save_submission(
    name: str,
    email: str,
    phone: str,
    message: str,
    ip: str | None,
    user_agent: str | None,
) -> int:
    """Uses the request.form values to add to the database as records"""
    init_db()
    created_at_utc = datetime.now(timezone.utc).isoformat()
    sql = """
    INSERT INTO contact_submissions (
        created_at_utc, name, email, phone, message, ip, user_agent
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute(
            sql,
            (created_at_utc, name, email, phone, message, ip, user_agent),
        )
        conn.commit()
        row_id = cur.lastrowid
        if row_id is None:
            raise RuntimeError("Insert failed: no row id returned.")

        return row_id


# status → UI message + Bootstrap alert class
STATUS_UI = {
    "success": {
        "title": "Form submission successful!",
        "message": "You should receive a confirmation on your email.",
        "alert_class": "alert-success",
    },
    "error": {
        "title": "Error sending message!",
        "message": "Ops, something went wrong. Please try again and fill all the fields.",
        "alert_class": "alert-danger",
    },
    "error_email": {
        "title": "Invalid email address!",
        "message": "Ops, you misspelled the email. Please use a valid email syntax.",
        "alert_class": "alert-danger",
    },
    "error_smtp": {
        "title": "Email service error!",
        "message": "We saved your request but could not send emails right now. \
            Please try again later.",
        "alert_class": "alert-danger",
    },
    "error_db": {
        "title": "Database error!",
        "message": "We could not save your message right now. Please try again later.",
        "alert_class": "alert-danger",
    },
}


def _status_payload(status: str | None) -> dict:
    """Return a dict with title/message/alert_class for the given status."""
    # if status is None:
    #     return {}
    return STATUS_UI.get(status or "", {})


def send_email(data):
    """Send email using email.message library to avoid ascii error making it safer"""
    if not GMAIL_SMTP or not MY_EMAIL or not MY_PASSWORD:
        raise RuntimeError("Missing SMTP env vars. Check your .env and load_dotenv()")

    email = EmailMessage()
    email["From"] = data["email_from"]
    email["To"] = data["email_to"]
    email["Subject"] = data["subject"]
    email.set_content(data["message"])

    with smtplib.SMTP(
        host=GMAIL_SMTP, port=587, timeout=30  # adding the port numbers solves the idle
    ) as connection:
        connection.starttls()
        connection.login(
            user=MY_EMAIL,
            password=MY_PASSWORD,
        )
        connection.send_message(email)


app = Flask(__name__)

# Initialize the repository
post_repo = PostRepository()


@app.route("/")
def index():
    """Render the homepage with the list of blog posts."""
    all_posts = post_repo.all_posts()
    return render_template("index.html", all_posts=all_posts)


@app.route("/about")
def about():
    """Serve the About page template."""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Serve the Contact page template."""
    status = request.args.get("status")
    ui = _status_payload(status=status)
    return render_template("contact.html", status=status, ui=ui)


@app.route("/contact/submit", methods=["POST"])
def contact_submit():
    """Submit data from the Contact page template."""
    name = (request.form.get("name") or "").strip()
    email = (request.form.get("email") or "").strip()
    phone = (request.form.get("phone") or "").strip()
    message = (request.form.get("message") or "").strip()

    # If any field is missing, redirect to back to contact with error status
    if not name or not email or not message:
        return redirect(url_for("contact", status="error"))
    elif "@" not in email:
        return redirect(url_for("contact", status="error_email"))
    else:
        # Capture request metadata (may be None)
        ip = request.headers.get("X-Forwarded-For", request.remote_addr)
        user_agent = request.headers.get("User-Agent")

        # Save to DB first (truth layer)
        try:
            submission_id = save_submission(
                name=name,
                email=email,
                phone=phone,
                message=message,
                ip=ip,
                user_agent=user_agent,
            )
            print(f"[contact_submit] saved submission id={submission_id}")
        except sqlite3.Error as exc:
            print(f"[contact_submit] db error: {exc}")
            return redirect(url_for("contact", status="error_db"))

        email_to_user = {
            "email_from": MY_EMAIL,
            "email_to": email,
            "subject": f"Welcome aboard, {name}!",
            "message": f"Hi {name},\n\
                Just to confirm that you are part of the community now.\n\n Take care ",
        }

        email_to_me = {
            "email_from": MY_EMAIL,
            "email_to": ZCH_MAIL,
            "subject": f"Added new user: {name}!",
            "message": f"New user added\n\
                name: '{name}'\nemail: {email}\nphone: {phone}\nmessage: {message}",
        }

        try:
            send_email(email_to_user)
            send_email(email_to_me)
            return redirect(url_for("contact", status="success"))
        except smtplib.SMTPException as exc:
            print(f"[contact_submit] email error: {exc}")
            return redirect(url_for("contact", status="error_smtp"))


@app.route("/post/<int:post_id>")
def post(post_id: int):
    """Serve the post detail page for the given post_id or 404 if missing."""
    post_data = post_repo.by_id(post_id)
    if post_data is None:
        abort(404)
    return render_template("post.html", post_data=post_data)


if __name__ == "__main__":
    app.run(debug=True)
