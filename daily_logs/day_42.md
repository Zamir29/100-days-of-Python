# Day 42 — HTML List & Birthday Invite
[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2042-Open%20Folder-blue)](../day_42/main.py)  

| **Scope** | **Description** |
|:---------:|:----------------|
|   Goal    | Learn ordered/unordered lists and build a simple birthday invitation webpage using basic HTML structure.          |
|   Steps   | Generate day_42, create index.html, practice `<ul>`/`<ol>`/`<li>` elements, add images/links, and build the birthday invite page following Angela’s instructions.         |
|   Stack   | VS Code, HTML, browser preview (generator script still Python).         |


## 📘 Table of contents
- [Day 42 — HTML List \& Birthday Invite](#day-42--html-list--birthday-invite)
  - [📘 Table of contents](#-table-of-contents)
  - [🧠 Concepts Learned](#-concepts-learned)
  - [⚠️ Challenges](#️-challenges)
  - [✅ Solutions / Insights](#-solutions--insights)
  - [📂 Project Structure](#-project-structure)
  - [🎯 Next Steps](#-next-steps)

---

## 🧠 Concepts Learned
* HTML list elements:
  * `<ul>` for unordered lists
  * `<ol>` for ordered lists
  * `<li>` for individual items

* Proper semantic nesting: nested lists must be placed inside an `<li>` element
* How browsers auto-correct invalid HTML vs. how linters enforce correct structure
* Adding images with `<img>` and meaningful alt text
* Creating hyperlinks with `<a href="...">`
* Using *Emmet abbreviations* in VS Code to generate boilerplate quickly
* Building a complete HTML “body” structure without needing full boilerplate


## ⚠️ Challenges
* Misplaced nested lists:  
  `<ul>` and `<ol>` placed directly inside another `<ul>` caused linter warnings

* Understanding why the browser renders the page anyway despite invalid structure
* Remembering correct indentation and hierarchy (h1 → h2 → h3)


## ✅ Solutions / Insights
* Learned the strict rule: `<ul>` and `<ol>` can only contain `<li>` (or script/template)
* Wrapped all nested lists properly inside parent `<li>` tags
* Realized how linters enforce best practices even when browsers are forgiving
* Built the birthday invite extremely fast thanks to good fundamentals + Emmet
* Reinforced heading semantics: don’t skip levels


## 📂 Project Structure
```
day_42/
├── 3.0 List Elements
│   ├── goal.png
│   └── index.html
├── 3.1 Nesting and Indentation
│   ├── goal.png
│   └── index.html
├── 3.2 Anchor Elements
│   ├── goal.png
│   └── index.html
├── 3.3 Image Elements
│   ├── goal1.png
│   ├── goal2.png
│   └── index.html
├── 3.4 Birthday Invite Project
│   ├── goal.png
│   └── index.html
├── config.py
└── main.py
```

## 🎯 Next Steps
* Move to Day 43 and begin learning CSS basics (color, fonts, alignment)
* Apply styles to the birthday invite page to make it visually appealing
* Start preparing for later lessons where HTML + CSS will integrate into Flask
* Keep using Emmet for fast scaffolding, but continue practicing semantic correctness manually


---
[![prev_day](https://img.shields.io/badge/⬅️_Day_41-grey?style=for-the-badge)](day_41.md) [![prev_day](https://img.shields.io/badge/Day_43_➡️-grey?style=for-the-badge)](day_43.md)
