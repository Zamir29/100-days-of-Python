# Day 71 — Deploy your WebApp <!-- omit in toc -->

[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2071-Open%20Folder-blue)](../day_71/main.py)

| **Scope** | **Description**                                                                    |
| :-------: | :--------------------------------------------------------------------------------- |
|   Goal    | Publish the Flask blog online (production deployment).                             |
|   Steps   | Push to GitHub → add Procfile/Gunicorn → deploy on Heroku → switch DB to Postgres. |
|   Stack   | Flask, Git/GitHub, Heroku, Gunicorn, PostgreSQL                                    |

## 📘 Table of contents <!-- omit in toc -->

- [🧠 Concepts Learned](#-concepts-learned)
- [⚠️ Challenges](#️-challenges)
- [✅ Solutions / Insights](#-solutions--insights)
- [📂 Project Structure](#-project-structure)
- [🏗 Architecture](#-architecture)
- [🎯 Next Steps](#-next-steps)

---

## 🧠 Concepts Learned

- Difference between development DB (SQLite) and production DB (PostgreSQL).
- How Gunicorn runs Flask apps in production instead of `app.run()`.
- How Render deploys from a specific Git branch.
- Importance of environment variables (`DATABASE_URL`) in production.
- How `db.create_all()` works (creates tables only if missing, does NOT migrate).
- Basic `psql` usage (`\dt`, `\d`, `SELECT`, `COUNT(*)`).
- Difference between SQLite CLI commands (`.tables`) and PostgreSQL meta-commands (`\dt`).
- Understanding free-tier limitations (cold starts, single instance, connection caps).
- Short-circuit behavior in Python conditionals (`user is None or ...`).

## ⚠️ Challenges

- Python 3.13 incompatibility with SQLAlchemy on Render.
- Understanding why model changes do not automatically update existing DB schema.
- Confusion between SQLite and PostgreSQL CLI commands.
- Setting up `psql` correctly on macOS (PATH configuration).
- Mental friction around infrastructure vs first paying client.
- Strategic confusion between engineering mastery and business validation.

## ✅ Solutions / Insights

- Downgraded Python to 3.12 for stable deployment.
- Installed PostgreSQL client via Homebrew and configured PATH safely.
- Connected to Render Postgres using external DB URL.
- Verified production tables directly with `psql`.
- Confirmed data integrity via manual SQL queries.
- Realized infrastructure is not the bottleneck for first revenue.
- Identified that clarity of objective (job vs SaaS vs mastery) matters more than infra optimization.

## 📂 Project Structure

```text
day_71/
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
    └── register.htm
```

## 🏗 Architecture

```mermaid
graph TD;
    Dev[Developer] -->|Commit and push| GitHub[GitHub repo];
    GitHub -->|Auto deploy on branch day_71| RenderDeploy[Render deploy];

    subgraph BuildPhase["Build on Render"]
        RenderDeploy -->|Root Directory = day_71| RootDir[Use subfolder];
        RootDir -->|Build command| BuildCmd[pip install -r requirements.txt];
        BuildCmd -->|Create runtime| PyEnv[Python environment];
        PyEnv -->|Start command| StartCmd[gunicorn main:app];
    end

    subgraph RuntimePhase["Runtime on Render"]
        StartCmd --> Gunicorn[Gunicorn WSGI server];
        Gunicorn --> FlaskApp[Flask app];
        FlaskApp --> Env[Load env vars<br/>DATABASE_URL<br/>SECRET_KEY<br/>PYTHON_VERSION];
        FlaskApp --> ORM[SQLAlchemy ORM];
        ORM -->|Connect via DATABASE_URL| Postgres[Render PostgreSQL];
    end

    User[Browser] -->|HTTP request| Gunicorn;
    Postgres -->|Query results| ORM;
    ORM --> FlaskApp;
    FlaskApp -->|HTML response| User;

    %% -- Color Style --
    classDef beige fill:#EDD3A6,stroke:#EAC78B,color:#222;
    classDef pink fill:#EBABB5,stroke:#E88F9D,color:#222;
    classDef mint fill:#ABE0D2,stroke:#74C1AD,color:#222;
    classDef blue fill:#83C8E8,stroke:#59BAE6,color:#222;
    classDef deepblue fill:#85B4D0,stroke:#007AC4,color:#222;
    classDef red fill:#FF814B,stroke:#B6000F,color:#222;
    classDef bluelight fill:#c4deea,stroke:#007AC4,color:#222;

    class Dev,User beige;
    class GitHub pink;
    class RenderDeploy,RootDir,BuildCmd,PyEnv,StartCmd mint;
    class Gunicorn,FlaskApp blue;
    class Env deepblue;
    class ORM red;
    class Postgres pink;
    class BuildPhase,RuntimePhase bluelight;
```

## 🎯 Next Steps

- Refactor README generation to use YAML + Jinja (single source of truth).
- Update repository payoff to reflect “start from Angela + add production habits” mindset.
- Add role-based authorization instead of `id == 1` admin logic.
- Introduce real schema evolution later via migrations (Flask-Migrate/Alembic).
- Add Stripe Checkout proof-of-concept (payment link first, webhooks later).
- Decide 6-month priority: engineering depth vs revenue vs job positioning.

---

[![prev_day](https://img.shields.io/badge/⬅️_Day_70-grey?style=for-the-badge)](day_70.md) [![next_day](https://img.shields.io/badge/Day_72_➡️-grey?style=for-the-badge)](day_72.md)
