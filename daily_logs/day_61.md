# Day 61 — Flask Validation & Login Gate <!-- omit in toc -->

[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2061-Open%20Folder-blue)](../day_61/main.py)  

| **Scope** | **Description** |
|:---------:|:----------------|
|   Goal    | Build advanced Flask forms using Flask-WTF with validation + CSRF, and gate a “secrets” page behind login.          |
|   Steps   | Install/configure Flask-WTF → create `LoginForm` with validators → render form in Jinja with CSRF token → validate on submit → allow/deny access to `/secrets`.         |
|   Stack   | `Python`, `Flask`, `Flask-WTF` (WTForms), `Jinja2`, `HTML`/`CSS`.         |

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
day_61/
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
[![prev_day](https://img.shields.io/badge/⬅️_Day_60-grey?style=for-the-badge)](day_60.md) [![next_day](https://img.shields.io/badge/Day_62_➡️-grey?style=for-the-badge)](day_62.md)
