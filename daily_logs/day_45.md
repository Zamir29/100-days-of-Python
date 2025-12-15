# Day 45 — Web Scraping with BeautifulSoup <!-- omit in toc -->

[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2045-Open%20Folder-blue)](../day_45/main.py)  

| **Scope** | **Description** |
|:---------:|:----------------|
|   Goal    | Learn how to scrape websites without an API using BeautifulSoup. Parse HTML, extract specific elements (movie titles, rankings), and build a custom dataset by navigating and searching through webpage structure.          |
|   Steps   | Generate day_45 folder; create main.py; install BeautifulSoup and requests; follow Angela’s tutorial to load a webpage, inspect HTML structure, parse with BeautifulSoup; practice extracting tags, attributes, and text; scrape Empire's Top 100 Movies list; save results into a Python list or file.         |
|   Stack   | Python, BeautifulSoup, requests, HTML inspection tools (browser DevTools), VS Code         |

## 📘 Table of contents <!-- omit in toc -->

- [🧠 Concepts Learned](#-concepts-learned)
- [⚠️ Challenges](#️-challenges)
- [✅ Solutions / Insights](#-solutions--insights)
- [📂 Project Structure](#-project-structure)
- [🏗 Architecture](#-architecture)
- [🎯 Next Steps](#-next-steps)

---

## 🧠 Concepts Learned

- How to use `requests.get()` to download a webpage and the difference between `response.text` (decoded string) and `response.content` (raw bytes).
- Basics of **BeautifulSoup**:
  - Creating a soup object with `BeautifulSoup(html, "html.parser")`
  - Using `.find()`, `.find_all()`, `.select_one()` to target specific tags and classes.
  - Extracting information with `.getText()` and `.get("href")`.
- How to read and reason about real-world HTML structure (Hacker News + Empire Online snapshot):
  - Using tag/class combos like `h3.title`.
  - Understanding how IDs (`id="46274822"` vs `id="score_46274822"`) logically link related elements (title ↔ score).
- Building structured Python data from scraped HTML:
  - Lists of dicts: `{"title": ..., "link": ..., "score": ...}`
  - Using **list comprehensions** for cleaner transformations.
- Reversing and slicing lists:
  - `movies = movies[::-1]`
  - `movies[:10]` for top 10 items.
- Using `max()` with a `key` function to find the highest-scoring article:
  - `max(enumerate(all_articles), key=lambda x: x[1]["score"])`.
- File writing fundamentals:
  - Difference between `"w"` (overwrite once at open) and `"a"` (append to existing content).
  - Why `with open(..., "w")` outside the loop is cleaner and more efficient than opening inside the loop.

## ⚠️ Challenges

- Confusion around file paths when running scripts from different directories:
  - Running `main.py` from the repo root vs from inside `day_45/` and why relative paths behaved differently.
- Hacker News HTML layout being different from Angela’s original version:
  - Original selectors (`.titleline`, `.score`) no longer matched the same way, forcing a deeper read of the HTML.
- Understanding how to reliably match a title with its corresponding score instead of just taking “the first title” and “the first score”.
- Misconception about `"w"` mode:
  - Initially thinking every `.write()` with `"w"` would overwrite the previous line, leaving only the last line in the file.
- Terminal workflow:
  - Realising that `mkdir Movie_Challenge && touch main.py` touches `main.py` in the **current directory**, not inside the new folder, unless the path is explicit.

## ✅ Solutions / Insights

- **File paths & execution context**  
  Learned that Python’s relative file paths are resolved from the **current working directory**, not from the script location. The correct mental model:
  - Shell location + script path + `open()` path all matter.
  - (Bonus from earlier: using `Path(__file__).resolve().parent` if I want paths relative to the script file.)

- **Robust Hacker News scraping**  
  Instead of relying on “first `.titleline` + first `.score`”, used the `id` pattern:
  - Article row: `<tr class="athing submission" id="46274822">`
  - Score span: `<span class="score" id="score_46274822">`
  - This allowed building a stable link `row_id → score_{row_id}` and extracting correct title/link/score combos.

- **Reversing movie order**  
  The Empire list was in reverse (100 → 1), so:
  - Built `movies = [row.getText() for row in rows]`
  - Then reversed with `movies = movies[::-1]`
  - This matched Angela’s approach and confirmed that the slice syntax was the right intuitive choice.

- **Top 10 extraction**  
  Once the list was in correct order, extracting top 10 became a trivial slice:
  - `top_ten = movies[:10]`
  - Saved into a separate `top10.txt` file.

- **Correct understanding of `"w"` vs `"a"`**  
  - `"w"` clears the file **once when opening**, then all `.write()` calls append sequentially in that session.
  - `"a"` keeps existing content and always appends to the end.
  - `"w"` is ideal for regenerating a full snapshot (like the movie list).
  - `"a"` is ideal for logs or accumulating entries over time.

- **Terminal one-liner insight**  
  - `mkdir Movie_Challenge && touch Movie_Challenge/main.py` is the correct way to create a folder *and* a file inside it in one line.
  - The shell does **not** change directory after `mkdir`, so paths must be explicit if I want to create files in the new folder.

## 📂 Project Structure

```text
day_45
├── Movie_Challenge
│   ├── main.py
│   ├── movies.txt
│   └── top10.txt
├── config.py
├── main.py
└── website.html
```

## 🏗 Architecture

```mermaid
graph TD;
    A[Start Day 45 Script] --> B[requests.get(URL)];
    B --> C[response.text (HTML)];
    C --> D[BeautifulSoup(html, "html.parser")];
    D --> E[find_all(h3.title) / find_all(tr.athing.submission)];
    E --> F[Extract titles, links, scores via list comprehension];
    F --> G[Transform data<br/>- reverse list<br/>- compute top 10<br/>- find max score];
    G --> H[Write results to files<br/>movies.txt / top10.txt];
    H --> I[Verify output length & sanity check in terminal];
```

## 🎯 Next Steps

- Refactor scraping code into small functions for cleaner structure:
  - `fetch_page(url)`, `parse_movies(html)`, `save_to_file(filename`, `movies)`, etc.
- Add basic error handling:
  - Handle network errors (e.g. `requests.exceptions.RequestException`). 
  - Gracefully handle missing elements instead of assuming the HTML is always perfect.
- Experiment with different selectors:
  - Try `.select()` and more complex CSS selectors instead of only `.find_all()`.
- Try scraping a different simple site:
  - Another ranking list (books, games, etc.) to reinforce the same pattern on a different HTML.
- (Later) Turn this into a small CLI:
  - Let the user choose how many top movies to save (top 10, 20, 50).  

---
[![prev_day](https://img.shields.io/badge/⬅️_Day_44-grey?style=for-the-badge)](day_44.md) [![next_day](https://img.shields.io/badge/Day_46_➡️-grey?style=for-the-badge)](day_46.md)
