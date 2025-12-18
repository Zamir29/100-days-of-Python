# 100 Days of Python – Angela Yu
[![Udemy](https://img.shields.io/badge/Udemy-Angela%20Yu's%20100%20Days%20of%20Python-A435F0?&logo=Udemy&logoColor=white)](https://www.udemy.com/course/100-days-of-code/)  
![](https://progress-bar.xyz/48/?scale=100&title=Progress&width=400&prefix=Day-&suffix=&progress_color=9CBF1F)  

![Repo Size](https://img.shields.io/github/repo-size/hashorva/100-days-of-Python) ![Code Frequency](https://img.shields.io/github/commit-activity/m/hashorva/100-days-of-Python)


This repository tracks my full journey through Angela's course on Python, including:

* Daily project folders (one per day)
* Personal Daily Logs documenting what I learned, stored in `/logs/`
* Notes, improvements, and refactoring as I progress from beginner → advanced

The stack I am using is:  
![Python](https://img.shields.io/badge/Python-3.11-blue) ![PyCharm](https://img.shields.io/badge/pycharm-143?&logo=pycharm&logoColor=black&color=black&labelColor=green) ![Claude](https://img.shields.io/badge/Claude-D97757?&logo=claude&logoColor=white) ![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?&logo=openai&logoColor=white)

**🏅 Focus:** Python · Automation · APIs · Tkinter · Data Handling  
**🎯 Goal:** Build senior-level fluency through 100 structured projects  
**📈 Next Steps (post-course):** Data Science fundamentals + Machine Learning (NumPy, Pandas, scikit-learn)

---
I’m building this as both a **learning archive** and a **public portfolio**.

---

## 📘 Table of Contents
* [📚 Daily Progress](#-daily-progress)
* [🏆 Current Progress](#-current-progress)
* [🧩 Highlights So Far](#-highlights-so-far)
* [🚀 Why This Repo Exists](#-why-this-repo-exists)
* [📌 Next Steps](#-next-steps)

## 📚 Daily Progress
[![Logs](https://img.shields.io/badge/Previous%20Logs-orange)](daily_logs/) 
![Last Updated](https://img.shields.io/github/last-commit/hashorva/100-days-of-Python)
- **Day 48 - Selenium WebDriver: Browser Automation & Advanced Web Scraping**   
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_48/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_48.md)  
Learn how Selenium WebDriver automates a real browser to interact with websites (type, click, scroll) beyond what BeautifulSoup can do. Use it to run repeatable “human-like” flows with Python.  
**Stack used:** `Python`, `Selenium`, `WebDriver` (ChromeDriver/SafariDriver), `VS Code`/`PyCharm`, `Chrome` or `Safari`.

<details><summary>Show all logs</summary>  

- **Day 47 - Amazon Price Tracker**   
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_47/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_47.md)  
Build a Python bot that checks an Amazon product page price and emails you when it drops below a target.  
**Stack used:** `Python`, `requests`, `BeautifulSoup`, `smtplib` (+ dotenv optional)


- **Day 46 - Spotify Musical Time Machine**   
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_46/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_46.md)  
Build a script that takes a past date, scrapes the Billboard Hot 100 for that day, and creates a Spotify playlist with those songs. Practice combining web scraping (BeautifulSoup) with a real-world API (Spotify).  
**Stack used:** Python, requests, BeautifulSoup, Spotify Web API (e.g. spotipy), python-dotenv, VS Code, web browser


- **Day 45 - Web Scraping with BeautifulSoup**   
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_45/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_45.md)  
Learn how to scrape websites without an API using BeautifulSoup. Parse HTML, extract specific elements (movie titles, rankings), and build a custom dataset by navigating and searching through webpage structure.  
**Stack used:** Python, BeautifulSoup, requests, HTML inspection tools (browser DevTools), VS Code


- **Day 44 - Advanced HTML & CSS — Divs, Spans, Box Model, Positioning**   
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_44/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_44.md)  
Learn how divs, spans, box model, and CSS positioning work. Build a more structured webpage layout following Angela’s teaching.  
**Stack used:** VS Code, HTML, CSS, web browser


- **Day 43 - CSS Selectors for Styled Webpage**   
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_43/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_43.md)  
Learn CSS selectors, link an external stylesheet, and style a multi-section HTML page to practice structure and presentation.  
**Stack used:** VS Code, HTML, CSS, web browser (Python only for the generator script).


- **Day 42 - HTML List & Birthday Invite**   
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_42/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_42.md)  
Learn ordered/unordered lists and build a simple birthday invitation webpage using basic HTML structure.  
**Stack used:** VS Code, HTML, browser preview (generator script still Python).


- **Day 41 - Introduction to HTML**   
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_41/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_41.md)  
Understand basic HTML structure and build a simple personal webpage following Angela's lesson.  
**Stack used:** VS Code, HTML, web browser (Python only for the generator script).


- **Day 40 - Capstone: Flight Club – Users & Email Alerts**   
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_40/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_40.md)  
Upgrade yesterday's personal flight deal finder into a multi-user "Flight Club" service. Let users sign up with name and email and receive cheap flight alerts automatically.  
**Stack used:** Python, requests, SMTP, Sheety API, flight search API (Amadeus/Tequila). Use environment variables for API keys and email credentials.


- **Day 39 - Flight Deal Finder**   
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_39/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_39.md)  
Build a tool that monitors flight prices and alerts you when they drop below a target price by querying a flight search API and comparing results to stored thresholds.  
**Stack used:** `Python`, `requests`, Tequila/Kiwi flight API, Google Sheets + Sheety, environment variables for API keys


- **Day 38 - Workout Tracking App w/ Google Sheet**   
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_38/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_38.md)  
Turn a natural-language workout description into structured data and log each exercise (date, time, duration, calories) into a Google Sheet.  
**Stack used:** Python 3, `requests`, `datetime`, environment variables, Exercise API, Sheety/Google Sheets.


- **Day 37 - Habit Tracking App**   
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_37/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_37.md)  
Build a small habit tracking tool that talks to an external API to log my daily habits (e.g. coding time) and visualize progress on a graph.  
**Stack used:** Python, requests, HTTP APIs (Pixela), environment variables (.env / python-dotenv), JSON


- **Day 36 - Trading News Alert Project**  
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_36/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_36.md)  
Today’s goal is to recreate the core features of a Bloomberg-style stock alert system.
The program fetches stock price movements, calculates percentage change, and—if the fluctuation is significant—pulls relevant news via a News API and sends an SMS alert through Twilio.  
**Stack used:** Python · APIs · HTTP Requests · JSON Parsing · News API · Twilio Messaging  


- **Day 35 - Keys, Auth & Environment Variables**  
  [![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_35/main.py)
  [![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_35.md)  
Today’s goal is to learn how to access protected APIs using authentication keys and how to keep credentials safe by loading them from environment variables instead of hard-coding them.  
**Stack used:** Python · APIs · `python-dotenv` · Environment Variables  


- **Day 34 - GUI Quiz App with API**  
[![Open Project Folder](https://img.shields.io/badge/Open-📁%20Folder-blue)](/day_34/main.py) 
[![Open Log File](https://img.shields.io/badge/Open-📝%20Log-orange)](/daily_logs/day_34.md) 
Today’s goal was to build a fully working GUI Quiz App using Tkinter, connected to a live trivia API.  
I learned how to structure a project with clear separation of concerns (data → logic → UI) and how to handle state changes, callbacks, and user feedback inside a GUI workflow.  
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

* Python fundamentals
* Conditionals & loops
* Functions & parameters
* OOP (Object-Oriented Programming)
* Working with JSON, CSV, and external files
* APIs & HTTP requests
* GUI apps with Tkinter
* Email automation
* Error handling
* Pandas basics

---

## 🚀 Why This Repo Exists

I’m using GitHub to:

* Make my progress visible
* Build software discipline (commit → push → log → repeat)
* Keep everything portable across machines
* Create a strong public portfolio showing consistent learning

---

## 📌 Next Steps

* Import all my existing Daily Logs
* Build a full Daily Log TOC
* Add screenshots or highlights for bigger projects
* Expand README as I progress

---

If you're attending the course too, feel free to explore the code and logs! 💡

---

> [!NOTES]  
> The main badges come from [Shields.io](https://shields.io/badges) website.  
> The progress bar comes from [Guibranco](https://github.com/guibranco/progressbar) repo.  
> The brand badges come from [Ileriayo](https://github.com/Ileriayo/markdown-badges) repo.  
> The other badges come from [henriquesebastiao](https://github.com/henriquesebastiao/badges) repo.  
> To create diagrams in .md file go to [Diagrams in Markdown](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams)