# Day 67 — Blog with RESTful editing <!-- omit in toc -->

[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2067-Open%20Folder-blue)](../day_67/main.py)

| **Scope** | **Description**                                                                                                           |
| :-------: | :------------------------------------------------------------------------------------------------------------------------ |
|   Goal    | Build a blog that reads posts from `posts.db` via Flask-SQLAlchemy and supports viewing + editing posts.                  |
|   Steps   | 1) Set up starter files. 2) Connect to `posts.db` with SQLAlchemy. 3) Build list + post pages. 4) Add create/edit/delete. |
|   Stack   | Python, Flask, Jinja2, SQLite, Flask-SQLAlchemy, Flask-WTF, CKEditor, Bootstrap.                                          |

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
day_67/
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

[![prev_day](https://img.shields.io/badge/⬅️_Day_66-grey?style=for-the-badge)](day_66.md) [![next_day](https://img.shields.io/badge/Day_68_➡️-grey?style=for-the-badge)](day_68.md)
