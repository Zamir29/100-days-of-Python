# 100 Days of Python – Angela Yu

[![Udemy](https://img.shields.io/badge/Udemy-Angela%20Yu's%20100%20Days%20of%20Python-A435F0?&logo=Udemy&logoColor=white)](https://www.udemy.com/course/100-days-of-code/)
![](https://progress-bar.xyz/74/?scale=100&title=Progress&width=400&prefix=Day-&suffix=&progress_color=9CBF1F)

![Repo Size](https://img.shields.io/github/repo-size/hashorva/100-days-of-Python) ![Code Frequency](https://img.shields.io/github/commit-activity/m/hashorva/100-days-of-Python)

This repository tracks my full journey through Angela's course on Python, including:

- Daily project folders (one per day)
- Personal Daily Logs documenting what I learned, stored in `/logs/`
- Notes, improvements, and refactoring as I progress from beginner → advanced

The stack I am using is:
![Python](https://img.shields.io/badge/Python-3.11-blue) ![PyCharm](https://img.shields.io/badge/pycharm-143?&logo=pycharm&logoColor=black&color=black&labelColor=green) ![Claude](https://img.shields.io/badge/Claude-D97757?&logo=claude&logoColor=white) ![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?&logo=openai&logoColor=white)

**🏅 Focus:** Python · Automation · APIs · Tkinter · Data Handling
**🎯 Goal:** Build senior-level fluency through 100 structured projects
**📈 Next Steps (post-course):** Data Science fundamentals + Machine Learning (NumPy, Pandas, scikit-learn)

---

I’m building this as both a **learning archive** and a **public portfolio**.

---

## 📘 Table of Contents

- [100 Days of Python – Angela Yu](#100-days-of-python--angela-yu)
  - [📘 Table of Contents](#-table-of-contents)
  - [📚 Daily Progress](#-daily-progress)
  - [🏆 Upcoming goal](#-upcoming-goal)
    - [🔸 **Next Milestone**](#-next-milestone)
    - [🔸 **Big Milestone**](#-big-milestone)
    - [🔹 **FINAL GOAL**](#-final-goal)
  - [🧩 Highlights So Far](#-highlights-so-far)
  - [🚀 Why This Repo Exists](#-why-this-repo-exists)
  - [📌 Next Steps](#-next-steps)

## 📚 Daily Progress

[![Logs](https://img.shields.io/badge/Previous%20Logs-orange)](daily_logs/)
![Last Updated](https://img.shields.io/github/last-commit/hashorva/100-days-of-Python)
- **Day 74 - Analyze LEGO Dataset**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_74/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_74.md)<br>
Analyze LEGO datasets with Pandas by aggregating, merging, and visualizing data to answer questions about set size, themes, yearly growth, and complexity over time.<br>
**Stack used:** Python, Pandas, Matplotlib, Jupyter Notebook or Google Colab, and CSV datasets.

<details><summary>Show all logs</summary>  

- **Day 73 - Data Visualization with Matplotlib**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_73/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_73.md)<br>
Analyze the evolution of programming language popularity over time using StackOverflow data by transforming raw CSV data into a structured time-series format and visualizing trends with line charts.<br>
**Stack used:** Python with Pandas for data manipulation and transformation, Matplotlib for data visualization, and Jupyter Notebook for exploratory analysis and iterative development of the workflow.


- **Day 72 - Data Exploration with Pandas**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_72/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_72.md)<br>
Analyze post-university salary data using Pandas to evaluate earning potential, risk, and category differences across college majors.<br>
**Stack used:** Python, Jupyter Notebook, Pandas, CSV dataset (PayScale survey data).



- **Day 71 - Deploy your WebApp**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_71/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_71.md)<br>
  Deploy your Flask blog on the public internet using Git/GitHub + Heroku + Gunicorn, and start upgrading the app from a dev setup (SQLite/local) to<br>
  **Stack used:** Flask, Git/GitHub, Heroku, Gunicorn, PostgreSQL


- **Day 70 - Git, Github and Version Control**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_70/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_70.md)<br>
  Understand Git/GitHub version control enough to work confidently with branches and merges.<br>
  **Stack used:** Git CLI, GitHub.

- **Day 69 - Blog Authorization**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_69/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_69.md)<br>
  Add user authentication and a comment system to the blog, with admin-only permissions for post management.<br>
  **Stack used:** Python, Flask, Flask-Login, Flask-WTF, SQLAlchemy, Werkzeug (password hashing), Jinja2, SQLite

- **Day 68 - Authentication with Flask**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_68/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_68.md)<br>
  Build secure authentication in Flask so users can register, log in and out, and access a protected “top-secret” download only when authenticated.<br>
  **Stack used:** Python, Flask, Flask-Login, Flask-SQLAlchemy (SQLite), Werkzeug Security (password hashing), Jinja2 templates, HTML/CSS (Bootstrap optional).

- **Day 67 - Blog with RESTful editing**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_67/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_67.md)<br>
  Build a blog that reads posts from `posts.db` via Flask-SQLAlchemy and supports viewing + editing posts.<br>
  **Stack used:** Python, Flask, Jinja2, SQLite, Flask-SQLAlchemy, Flask-WTF, CKEditor, Bootstrap.

- **Day 66 - Build REST API Service**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_66/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_66.md)<br>
  Build a REST API with Flask that exposes your own dataset through JSON endpoints and supports basic create/read/update/delete operations.<br>
  **Stack used:** Python, Flask, REST/JSON, HTTP methods (GET/POST/PATCH/DELETE), SQLAlchemy + SQLite, environment variables for API keys.

- **Day 65 - Web Design Principles**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_65/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_65.md)<br>
  Learn the core principles of web design so your websites don't just work, but look beautiful and feel premium. Understand how design shapes first impressions and perceived value within seconds.<br>
  **Stack used:** Web design fundamentals, HTML/CSS (as the medium), visual design principles (color, type), UI patterns, UX thinking.

- **Day 64 - Top 10 Movies**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_64/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_64.md)<br>
  Build a "Top 10 Movies" Flask website where you can add movies, store them in SQLite via SQLAlchemy, and edit/update entries through WTForms.<br>
  **Stack used:** `Python`, `Flask`, `Jinja2` templates, `WTForms`/`Flask-WTF`, `SQLite`, `SQLAlchemy` (`Flask-SQLAlchemy`).

- **Day 63 - Virtual Bookshelf with SQLite/SQLAlchemy**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_63/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_63.md)<br>
  Build a Flask app that stores and manages data in a SQLite database using SQLAlchemy (create, read, update, delete).<br>
  **Stack used:** `Python`, `Flask`, `Jinja2`, `SQLite`, `Flask-SQLAlchemy` (SQLAlchemy ORM)

- **Day 62 - Coffee & WiFi Project**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_62/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_62.md)<br>
  Build a Flask app that collects café data via validated web forms and stores it in a real database for reliable retrieval and display.<br>
  **Stack used:** `Python`, `Flask`, `Jinja2`, `Flask-WTF`/`WTForms`, `Bootstrap` (or `Bootstrap-Flask`), `SQLite`, `SQLAlchemy` (`Flask-SQLAlchemy`).

- **Day 61 - Flask Validation & Login Gate**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_61/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_61.md)<br>
  Build advanced Flask forms using Flask-WTF with validation + CSRF, and gate a "secrets" page behind login.<br>
  **Stack used:** `Python`, `Flask`, `Flask-WTF` (WTForms), `Jinja2`, `HTML`/`CSS`.

- **Day 60 - Bootstrap + Flask POST Form**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_60/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_60.md)<br>
  Reuse the Day 59 Flask + Bootstrap blog and add HTML forms with POST handling to collect user input and respond dynamically.<br>
  **Stack used:** Python, Flask, Jinja2, HTML forms, Bootstrap, HTTP GET/POST.

- **Day 59 - Bootstrap + Flask blog**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_59/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_59.md)<br>
  Upgrade my Flask blog using a free Bootstrap template to make it multi-page, mobile-responsive, and able to render dynamic post pages with full-screen titles.<br>
  **Stack used:** Python, Flask, Jinja2, Bootstrap 5, HTML/CSS, JavaScript, VS Code/PyCharm.

- **Day 58 - Bootstrap Setup**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_58/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_58.md)<br>
  Style my Flask blog using Bootstrap to achieve a clean, responsive layout with reusable templates (base.html) and consistent UI components.<br>
  **Stack used:** Python, Flask, Jinja2, HTML, CSS, Bootstrap 5 (CDN)

- **Day 57 - Templating with Jinja in Flask Apps**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_57/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_57.md)<br>
  Learn how to build more advanced Flask apps by using Jinja templating to create reusable page layouts and inject dynamic content. Render different pages (e.g. blog posts) from the same template structure.<br>
  **Stack used:** `Python`, `Flask`, `Jinja2` templating, `HTML`/`CSS`, dynamic routing with URLs, browser-based rendering.

- **Day 56 - Flask - Render HTML/Static files & Website Templates**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_56/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_56.md)<br>
  Build a Flask website that renders real HTML templates instead of plain text. Learn how to serve and link static assets (CSS + images) to style the pages properly.<br>
  **Stack used:** `Python`,` Flask`, `Jinja2` templates, `HTML`, `CSS`. Static assets via Flask `static/` + `url_for`, running locally with `VS Code`/`PyCharm` and a browser.

- **Day 55 - HTML & URL Parsing in Flask**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_55/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_55.md)<br>
  Build a Flask app that renders styled HTML pages and reacts to user guesses passed via the URL.<br>
  **Stack used:** Python, Flask, Jinja2 templates, HTML/CSS, static assets (GIFs).

- **Day 54 - Intro to Flask**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_54/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_54.md)<br>
  Build my first backend-powered website using Flask and understand the client–server–database model behind modern web apps.<br>
  **Stack used:** `Python`, `Flask`, `pip/venv`, `command line`, `VS Code`/`PyCharm`, web browser (`Chrome`/`Safari`)

- **Day 53 - Data Entry Job Automation**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_53/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_53.md)<br>
  Scrape rent listings (price, address, link) from the Zillow Clone and auto-submit each entry into a Google Form to generate a spreadsheet.<br>
  **Stack used:** `Python`, `requests`, `BeautifulSoup4`, `Selenium` + `WebDriver` (`Chrome`), `Google Forms` (+ `Google Sheets` via Responses tab).

- **Day 52 - Instagram Follower Bot**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_52/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_52.md)<br>
  Build an Instagram follower bot with Selenium that logs in and follows users from a target account's follower list. Keep it stable with explicit waits and safe follow limits.<br>
  **Stack used:** `Python`, `Selenium WebDriver`, `ChromeDriver` (or `Safari` on macOS). Optional: `python-dotenv` for credentials.

- **Day 51 - Internet Speed Twitter Complain Bot**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_51/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_51.md)<br>
  Build an automated "Internet Speed Complaint" bot that uses Selenium to run a Speedtest, captures download/upload results, compares them to promised speeds, and posts a complaint tweet when the speed is below the guarantee.<br>
  **Stack used:** `Python`, `Selenium WebDriver` (`Chrome`/`Safari`), `speedtest.net`, X/Twitter web app. Environment variables (`.env`) for credentials and promised speed thresholds.

- **Day 50 - Day 50 - Auto Tinder Swiping Bot**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_50/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_50.md)<br>
  Build a Selenium automation script that logs into Tinder on the web, handles popups/permissions, and performs automated swipes in a controlled loop.<br>
  **Stack used:** `Python`, `Selenium WebDriver`, `Chrome` (or `Safari`) + `WebDriver`/`Selenium Manager`, `VS Code`/`PyCharm`.

- **Day 49 - Automating Gym Class Bookings with Selenium (Snack & Lift)**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_49/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_49.md)<br>
  Automate a real browser with Selenium to log in and book gym classes on the Snack & Lift site. Practice reliable element waits, handling dynamic UI states (book/full/waitlist), and building resilient automation.<br>
  **Stack used:** `Python`, `Selenium WebDriver`, Google Chrome + ChromeDriver (persistent profile), `WebDriverWait`/`Expected Conditions`. Local Snack & Lift practice website (browser storage / `IndexedDB`).

- **Day 48 - Selenium WebDriver: Browser Automation & Advanced Web Scraping**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_48/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_48.md)<br>
  Learn how Selenium WebDriver automates a real browser to interact with websites (type, click, scroll) beyond what BeautifulSoup can do. Use it to run repeatable "human-like" flows with Python.<br>
  **Stack used:** `Python`, `Selenium`, `WebDriver` (ChromeDriver/SafariDriver), `VS Code`/`PyCharm`, `Chrome` or `Safari`.

- **Day 47 - Amazon Price Tracker**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_47/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_47.md)<br>
  Build a Python bot that checks an Amazon product page price and emails you when it drops below a target.<br>
  **Stack used:** `Python`, `requests`, `BeautifulSoup`, `smtplib` (+ dotenv optional)

- **Day 46 - Spotify Musical Time Machine**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_46/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_46.md)<br>
  Build a script that takes a past date, scrapes the Billboard Hot 100 for that day, and creates a Spotify playlist with those songs. Practice combining web scraping (BeautifulSoup) with a real-world API (Spotify).<br>
  **Stack used:** Python, requests, BeautifulSoup, Spotify Web API (e.g. spotipy), python-dotenv, VS Code, web browser

- **Day 45 - Web Scraping with BeautifulSoup**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_45/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_45.md)<br>
  Learn how to scrape websites without an API using BeautifulSoup. Parse HTML, extract specific elements (movie titles, rankings), and build a custom dataset by navigating and searching through webpage structure.<br>
  **Stack used:** Python, BeautifulSoup, requests, HTML inspection tools (browser DevTools), VS Code

- **Day 44 - Advanced HTML & CSS — Divs, Spans, Box Model, Positioning**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_44/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_44.md)<br>
  Learn how divs, spans, box model, and CSS positioning work. Build a more structured webpage layout following Angela's teaching.<br>
  **Stack used:** VS Code, HTML, CSS, web browser

- **Day 43 - CSS Selectors for Styled Webpage**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_43/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_43.md)<br>
  Learn CSS selectors, link an external stylesheet, and style a multi-section HTML page to practice structure and presentation.<br>
  **Stack used:** VS Code, HTML, CSS, web browser (Python only for the generator script).

- **Day 42 - HTML List & Birthday Invite**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_42/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_42.md)<br>
  Learn ordered/unordered lists and build a simple birthday invitation webpage using basic HTML structure.<br>
  **Stack used:** VS Code, HTML, browser preview (generator script still Python).

- **Day 41 - Introduction to HTML**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_41/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_41.md)<br>
  Understand basic HTML structure and build a simple personal webpage following Angela's lesson.<br>
  **Stack used:** VS Code, HTML, web browser (Python only for the generator script).

- **Day 40 - Capstone: Flight Club – Users & Email Alerts**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_40/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_40.md)<br>
  Upgrade yesterday's personal flight deal finder into a multi-user "Flight Club" service. Let users sign up with name and email and receive cheap flight alerts automatically.<br>
  **Stack used:** Python, requests, SMTP, Sheety API, flight search API (Amadeus/Tequila). Use environment variables for API keys and email credentials.

- **Day 39 - Flight Deal Finder**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_39/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_39.md)<br>
  Build a tool that monitors flight prices and alerts you when they drop below a target price by querying a flight search API and comparing results to stored thresholds.<br>
  **Stack used:** `Python`, `requests`, Tequila/Kiwi flight API, Google Sheets + Sheety, environment variables for API keys

- **Day 38 - Workout Tracking App w/ Google Sheet**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_38/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_38.md)<br>
  Turn a natural-language workout description into structured data and log each exercise (date, time, duration, calories) into a Google Sheet.<br>
  **Stack used:** Python 3, `requests`, `datetime`, environment variables, Exercise API, Sheety/Google Sheets.

- **Day 37 - Habit Tracking App**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_37/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_37.md)<br>
  Build a small habit tracking tool that talks to an external API to log my daily habits (e.g. coding time) and visualize progress on a graph.<br>
  **Stack used:** Python, requests, HTTP APIs (Pixela), environment variables (.env / python-dotenv), JSON

- **Day 36 - Trading News Alert Project**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_36/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_36.md)<br>
  Today's goal is to recreate the core features of a Bloomberg-style stock alert system.<br>
  The program fetches stock price movements, calculates percentage change, and—if the fluctuation is significant—pulls relevant news via a News API and sends an SMS alert through Twilio.<br>
  **Stack used:** Python · APIs · HTTP Requests · JSON Parsing · News API · Twilio Messaging

- **Day 35 - Keys, Auth & Environment Variables**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_35/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_35.md)<br>
  Today's goal is to learn how to access protected APIs using authentication keys and how to keep credentials safe by loading them from environment variables instead of hard-coding them.<br>
  **Stack used:** Python · APIs · `python-dotenv` · Environment Variables

- **Day 34 - GUI Quiz App with API**<br>
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_34/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_34.md)<br>
  Today's goal was to build a fully working GUI Quiz App using Tkinter, connected to a live trivia API.<br>
  I learned how to structure a project with clear separation of concerns (data → logic → UI) and how to handle state changes, callbacks, and user feedback inside a GUI workflow.<br>
  **Stack used:** Python · Tkinter · APIs · OOP (QuizBrain + UI) · JSON Parsing

</details>

---

## 🏆 Upcoming goal

### 🔸 **Next Milestone**

**Day 45** — Working on Intermediate Python Projects

### 🔸 **Big Milestone**

**Day 82** — Portfolio-ready Project

### 🔹 **FINAL GOAL**

Complete all 100 days with full logs and code history.

---

## 🧩 Highlights So Far

- Python fundamentals
- Conditionals & loops
- Functions & parameters
- OOP (Object-Oriented Programming)
- Working with JSON, CSV, and external files
- APIs & HTTP requests
- GUI apps with Tkinter
- Email automation
- Error handling
- Pandas basics

---

## 🚀 Why This Repo Exists

I’m using GitHub to:

- Make my progress visible
- Build software discipline (commit → push → log → repeat)
- Keep everything portable across machines
- Create a strong public portfolio showing consistent learning

---

## 📌 Next Steps

- Import all my existing Daily Logs
- Build a full Daily Log TOC
- Add screenshots or highlights for bigger projects
- Expand README as I progress

---

If you're attending the course too, feel free to explore the code and logs! 💡

---

> [!NOTE]
> The main badges come from [Shields.io](https://shields.io/badges) website.<br>
> The progress bar comes from [Guibranco](https://github.com/guibranco/progressbar) repo.<br>
> The brand badges come from [Ileriayo](https://github.com/Ileriayo/markdown-badges) repo.<br>
> The other badges come from [henriquesebastiao](https://github.com/henriquesebastiao/badges) repo.<br>
> To create diagrams in .md file go to [Diagrams in Markdown](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams)
