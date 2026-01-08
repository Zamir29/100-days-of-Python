# Day 52 — Instagram Follower Bot <!-- omit in toc -->

[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2052-Open%20Folder-blue)](../day_52/main.py)  

| **Scope** | **Description** |
|:---------:|:----------------|
|   Goal    | Build an Instagram follower bot with Selenium that logs in and follows users from a target account’s follower list. Keep it stable with explicit waits and safe follow limits.          |
|   Steps   | Automate login and handle cookie/“Not now” popups. Open a target profile, load followers by scrolling the modal, and click Follow in a controlled loop.         |
|   Stack   | `Python`, `Selenium WebDriver`, `ChromeDriver` (or `Safari` on macOS). Optional: `python-dotenv` for credentials.         |

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
day_52/
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
[![prev_day](https://img.shields.io/badge/⬅️_Day_51-grey?style=for-the-badge)](day_51.md) [![next_day](https://img.shields.io/badge/Day_53_➡️-grey?style=for-the-badge)](day_53.md)
