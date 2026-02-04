# Day 66 — Build REST API Service <!-- omit in toc -->

[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2066-Open%20Folder-blue)](../day_66/main.py)  

| **Scope** | **Description** |
|:---------:|:----------------|
|   Goal    | Build a REST API with Flask that exposes your own dataset through JSON endpoints and supports basic create/read/update/delete operations.          |
|   Steps   | Define Flask routes for public data retrieval, protect write actions with an API key, then implement CRUD endpoints (GET/POST/PATCH/DELETE) backed by a simple database model.         |
|   Stack   | Python, Flask, REST/JSON, HTTP methods (GET/POST/PATCH/DELETE), SQLAlchemy + SQLite, environment variables for API keys.         |

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
day_66/
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
[![prev_day](https://img.shields.io/badge/⬅️_Day_65-grey?style=for-the-badge)](day_65.md) [![next_day](https://img.shields.io/badge/Day_67_➡️-grey?style=for-the-badge)](day_67.md)
