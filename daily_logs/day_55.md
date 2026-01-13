# Day 55 — HTML & URL Parsing in Flask <!-- omit in toc -->

[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2055-Open%20Folder-blue)](../day_55/main.py)  

| **Scope** | **Description** |
|:---------:|:----------------|
|   Goal    | Build a Flask app that renders styled HTML pages and reacts to user guesses passed via the URL.          |
|   Steps   | Create routes for home and dynamic guesses, compare against a random number, and render the correct HTML + GIF response for low/high/correct.         |
|   Stack   | Python, Flask, Jinja2 templates, HTML/CSS, static assets (GIFs).         |

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
day_55/
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
[![prev_day](https://img.shields.io/badge/⬅️_Day_54-grey?style=for-the-badge)](day_54.md) [![next_day](https://img.shields.io/badge/Day_56_➡️-grey?style=for-the-badge)](day_56.md)
