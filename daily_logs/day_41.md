# Day 41 — Introduction to HTML
[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2041-Open%20Folder-blue)](../day_41/main.py)  

| **Scope** | **Description** |
|:---------:|:----------------|
|   Goal    | Understand basic HTML structure and build a simple personal webpage following Angela's lesson.          |
|   Steps   | Generate day_41, create index.html, follow Angela to add headings/text/links, then open the page in the browser to verify it works.         |
|   Stack   | VS Code, HTML, web browser (Python only for the generator script).         |


## 📘 Table of contents
- [Day 41 — Introduction to HTML](#day-41--introduction-to-html)
  - [📘 Table of contents](#-table-of-contents)
  - [🧠 Concepts Learned](#-concepts-learned)
  - [⚠️ Challenges](#️-challenges)
  - [✅ Solutions / Insights](#-solutions--insights)
  - [📂 Project Structure](#-project-structure)
  - [🏗 Architecture](#-architecture)
  - [🎯 Next Steps](#-next-steps)

---

## 🧠 Concepts Learned
- Refreshed the absolute basics of HTML structure (doctype, html/head/body).
- Reviewed semantic elements like headings, paragraphs, void elements (`<hr />`).
- Reinforced the idea that HTML is purely structural and intentionally minimal at this stage.
- Practiced writing a small, clean static page following a consistent hierarchy.
- Understood VS Code workflow for editing and previewing HTML without relying on PyCharm.


## ⚠️ Challenges
- No technical difficulty — the lesson was intentionally simple compared to the heavy API/code days before.
- Adjusting mentally from PyCharm’s Python-only workflow to VS Code’s multi-language environment.
- Minor friction understanding how Prettier formats HTML differently from Angela’s teaching style.
- Git identity confusion after seeing `Zamir29` still appear in GitLens.


## ✅ Solutions / Insights
- Accepted that today’s simplicity is part of Angela’s progression toward Flask and backend ↔ frontend integration.
- Learned how VS Code handles formatting (Prettier) and why indentation is structural, not semantic.
- Clarified the difference between `git user.name`, `user.email`, and GitHub username (`hashorva`) — understanding that email, not name, determines commit ownership.
- Set up a clean VS Code workflow, including GitLens and icons, making the environment more enjoyable and productive.


## 📂 Project Structure
```
day_41/
├── 2.1 Heading Element
│   ├── goal_headings.png
│   └── index.html
├── 2.2 Paragraph Element
│   ├── goal_paragraphs.png
│   └── index.html
├── 2.3 Void Elements
│   ├── goal_void.png
│   └── index.html
├── 2.4 Movie Ranking Project
│   └── index.html
├── config.py
└── main.py
```

## 🏗 Architecture
```mermaid
graph TD;
    User[User opens index.html in browser]
        --> Browser[Browser interprets HTML structure]
        --> Render[Render headings, paragraphs, and layout]
        --> Output[Static webpage displaying movie ranking]
```

## 🎯 Next Steps
- Continue Angela’s HTML/CSS days with VS Code to build comfort before Flask templates arrive.
- Practice keyboard-only navigation in VS Code to build speed and reduce mouse usage.
- Keep using GitLens + no-ff merges to clearly document daily progression.
- Optional: explore semantic grouping (`<main>`, `<section>`) as pages become more complex — not required now.

---
[![prev_day](https://img.shields.io/badge/⬅️_Day_40-grey?style=for-the-badge)](day_40.md) [![prev_day](https://img.shields.io/badge/Day_42_➡️-grey?style=for-the-badge)](day_42.md)
