# Day 38 — Workout Tracking App w/ Google Sheet
[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2038-Open%20Folder-blue)](../day_38/main.py)  

| **Scope** | **Description**                                                                                                                              |
|:---------:|:---------------------------------------------------------------------------------------------------------------------------------------------|
|   Goal    | Turn a natural-language workout description into structured data and log each exercise (date, time, duration, calories) into a Google Sheet. |
|   Steps   | Send the user’s sentence to the Exercise API, then POST each parsed exercise with timestamp and calories to the Google Sheets API.           |
|   Stack   | Python 3, `requests`, `datetime`, environment variables, Exercise API, Sheety/Google Sheets.                                                 |


## 📘 Table of contents
* [🧠 Concepts Learned](#-concepts-learned)
* [⚠️ Challenges](#-challenges)
* [✅ Solutions / Insights](#-solutions--insights)
* [🏗 Architecture](#-architecture)
* [🎯 Next steps](#-next-steps)

---

## 🧠 Concepts Learned

(Write bullet points here)

## ⚠️ Challenges

(What was confusing / hard)

## ✅ Solutions / Insights

(How you solved it / what finally clicked)

## 📂 Project Structure
```
day_38/
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
[![prev_day](https://img.shields.io/badge/⬅️_Day_37-grey?style=for-the-badge)](day_37.md) [![prev_day](https://img.shields.io/badge/Day_39_➡️-grey?style=for-the-badge)](day_39.md)
