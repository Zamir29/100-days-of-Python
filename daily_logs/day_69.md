# Day 69 — Blog Authorization <!-- omit in toc -->

[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2069-Open%20Folder-blue)](../day_69/main.py)  

| **Scope** | **Description** |
|:---------:|:----------------|
|   Goal    | Add user authentication and a comment system to the blog, with admin-only permissions for post management.          |
|   Steps   | Implement register/login/logout, protect routes with Flask-Login, add comments linked to users and posts, and restrict create/edit/delete to admin.         |
|   Stack   | Python, Flask, Flask-Login, Flask-WTF, SQLAlchemy, Werkzeug (password hashing), Jinja2, SQLite         |

## 📘 Table of contents <!-- omit in toc -->

- [🧠 Concepts Learned](#-concepts-learned)
- [⚠️ Challenges](#️-challenges)
- [✅ Solutions / Insights](#-solutions--insights)
- [📂 Project Structure](#-project-structure)
- [🏗 Architecture](#-architecture)
- [🎯 Next Steps](#-next-steps)

---

## 🧠 Concepts Learned

(Write bullet points here)

## ⚠️ Challenges

(What was confusing / hard)

## ✅ Solutions / Insights

(How you solved it / what finally clicked)

## 📂 Project Structure

```text
day_69/
├── main.py
├── config.py
```

## 🏗 Architecture

```mermaid
graph TD;
    Start([User Input]) --> Process{Check Condition};
    Process -->|Yes| Result[Success];
    Process -->|No| Error[Raise Exception];
```

## 🎯 Next Steps

(Refactors, extra features, things to revisit)  

---
[![prev_day](https://img.shields.io/badge/⬅️_Day_68-grey?style=for-the-badge)](day_68.md) [![next_day](https://img.shields.io/badge/Day_70_➡️-grey?style=for-the-badge)](day_70.md)
