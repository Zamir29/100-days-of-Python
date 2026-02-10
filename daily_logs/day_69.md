# Day 69 — Blog Authorization <!-- omit in toc -->

[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2069-Open%20Folder-blue)](../day_69/main.py)

| **Scope** | **Description**                                                                                                                                     |
| :-------: | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
|   Goal    | Add user authentication and a comment system to the blog, with admin-only permissions for post management.                                          |
|   Steps   | Implement register/login/logout, protect routes with Flask-Login, add comments linked to users and posts, and restrict create/edit/delete to admin. |
|   Stack   | Python, Flask, Flask-Login, Flask-WTF, SQLAlchemy, Werkzeug (password hashing), Jinja2, SQLite                                                      |

## 📘 Table of contents <!-- omit in toc -->

- [🧠 Concepts Learned](#-concepts-learned)
- [⚠️ Challenges](#️-challenges)
- [✅ Solutions / Insights](#-solutions--insights)
- [📂 Project Structure](#-project-structure)
- [🏗 Architecture](#-architecture)
- [🎯 Next Steps](#-next-steps)

---

## 🧠 Concepts Learned

- Implemented user authentication with **Flask-Login**: register, login, logout, `current_user`, and session-based auth.
- Understood the difference between **authentication** (who you are) and **authorization** (what you can do).
- Learned how Python **decorators** work (functions wrapping functions):
  - `@decorator` is syntactic sugar for `func = decorator(func)`.
  - Decorator **order** matters (`@A` above `@B` means `func = A(B(func))`).
  - Why `@wraps` preserves function metadata (name/docstring) and avoids Flask routing/debug surprises.
- Built an `admin_only` decorator and combined it with `@login_required` for clean access control.
- Switched the blog to a **relational** schema with SQLAlchemy:
  - Primary keys (PK) and foreign keys (FK) as stable identity links.
  - `author_id` in `BlogPost` as FK → `users.id`.
  - `post_id` and `author_id` in `Comment` as FK links.
- Understood that `relationship()` is **not a DB column**; it’s an ORM navigation layer built on top of FK columns.
- Used ORM relationships instead of manual queries (e.g., `post.comments` automatically filters by `post_id`).
- Rendered related objects in Jinja with relationship attributes (e.g., `post.author.name`).
- Implemented categorized flash messages (e.g., `success`, `warning`, `danger`) and Bootstrap alert styling.

## ⚠️ Challenges

- Confusion between what lives in the **database** vs what lives in the **ORM** (FK columns vs `relationship()` attributes).
- Schema mismatch after changing models (existing SQLite DB had no `author_id` / comment tables).
- Understanding why `author=current_user` works only when `BlogPost.author` is a relationship (not a string column).
- WTForms email validation error: missing dependency `email_validator`.
- Redirect vs render behavior (POST/redirect/GET) and why browsers prompt to “resend form” on refresh.
- Avoiding double flash messages after register/login redirects.
- Decorator layering: `@wraps` vs `@login_required` and how wrapping order affects the final callable.

## ✅ Solutions / Insights

- Fixed email validation by installing `email_validator` (required for WTForms `Email()` validator).
- Adopted the **PRG pattern**: after successful POST, `redirect()` to a GET route to prevent form resubmission popups.
- Implemented flash **categories** and rendered them as Bootstrap alerts via `get_flashed_messages(with_categories=True)`.
- Avoided duplicate flashes using a query-flag pattern (e.g., `?just_registered=1`) or suppressing secondary flashes.
- Rebuilt the database after schema changes by deleting the old SQLite file and recreating tables (tutorial-friendly alternative to migrations).
- Switched from storing author as text to storing identity:
  - DB stores `author_id`.
  - ORM provides `post.author` (User object) → templates use `post.author.name`.
- Leveraged relationships to avoid manual filtering:
  - `post.comments` replaces `SELECT Comment WHERE post_id = ...`.
- Built `admin_only` as a transparent wrapper forwarding `*args, **kwargs` and using `abort(403)` for forbidden access.
- Kept UI conditions (hide buttons in templates) as UX-only, with real security enforced server-side via decorators.

## 📂 Project Structure

```text
day_69/
├── config.py
├── forms.py
├── instance
│   └── blog.db
├── main.py
├── requirements.txt
├── static
│   ├── assets
│   │   ├── favicon.ico
│   │   └── img
│   │       ├── about-bg.jpg
│   │       ├── angela-profile.jpg
│   │       ├── contact-bg.jpg
│   │       ├── default-profile.jpg
│   │       ├── edit-bg.jpg
│   │       ├── home-bg.jpg
│   │       ├── login-bg.jpg
│   │       ├── post-bg.jpg
│   │       └── register-bg.jpg
│   ├── css
│   │   └── styles.css
│   └── js
│       └── scripts.js
└── templates
    ├── about.html
    ├── contact.html
    ├── footer.html
    ├── header.html
    ├── index.html
    ├── login.html
    ├── make-post.html
    ├── post.html
    └── register.html
```

## 🏗 Architecture

```mermaid
graph TD;
    U[Browser] -->|GET /| H[Home Route];
    U -->|GET /post/<id>| P[Post Route];

    U -->|GET/POST /register| R[Register Route];
    U -->|GET/POST /login| L[Login Route];
    U -->|GET /logout| O[Logout Route];

    R -->|create user + hash pw| DB[#40;SQLite via SQLAlchemy#41;];
    L -->|verify pw + login_user| DB;
    O -->|logout_user| H;

    H -->|select posts| DB;
    P -->|select post + comments| DB;

    P -->|POST comment| C[Create Comment];
    C -->|author_id + post_id| DB;

    U -->|admin-only create/edit| A[Protected Routes];
    A -->|@admin_only + @login_required| DB;
```

## 🎯 Next Steps

- Optional: move comment ordering into the relationship/query (instead of reversing in Jinja).
- Optional: add basic migrations (Alembic/Flask-Migrate) when ready to stop deleting SQLite DB files.
- Refactor template includes (ensure `header.html` doesn’t close `</body></html>` if it’s an include).
- Add rate-limiting / spam protection to comments (basic cooldown or captcha) as a stretch.
- Improve error messages and UX for auth flows (keep security-friendly generic login failure message).

---

[![prev_day](https://img.shields.io/badge/⬅️_Day_68-grey?style=for-the-badge)](day_68.md) [![next_day](https://img.shields.io/badge/Day_70_➡️-grey?style=for-the-badge)](day_70.md)
