# Day 51 — Internet Speed Twitter Complain Bot <!-- omit in toc -->

[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2051-Open%20Folder-blue)](../day_51/main.py)  

| **Scope** | **Description** |
|:---------:|:----------------|
|   Goal    | Build an automated “Internet Speed Complaint” bot that uses Selenium to run a Speedtest, captures download/upload results, compares them to promised speeds, and posts a complaint tweet when the speed is below the guarantee.          |
|   Steps   | Use Selenium to open speedtest.net, click “Go”, wait for the test to finish, and extract the download/upload values (and result ID if available). If the measured speeds are under the promised thresholds, automate logging into X/Twitter and publish a formatted complaint tweet to the provider’s handle.         |
|   Stack   | `Python`, `Selenium WebDriver` (`Chrome`/`Safari`), `speedtest.net`, X/Twitter web app. Environment variables (`.env`) for credentials and promised speed thresholds.         |

## 📘 Table of contents <!-- omit in toc -->

- [🧠 Concepts Learned](#-concepts-learned)
- [⚠️ Challenges](#️-challenges)
- [✅ Solutions / Insights](#-solutions--insights)
- [📂 Project Structure](#-project-structure)
- [🏗 Architecture](#-architecture)
- [🎯 Next Steps](#-next-steps)

---

## 🧠 Concepts Learned

- **Explicit waits beat `sleep()`**: using `WebDriverWait` + `expected_conditions` to synchronize with UI state (clickable / visible / present).
- **Polling for “real” values**: reading a value that starts as `—`/empty and becomes numeric later (loop + timeout).
- **Parsing + validating UI text**: convert strings to floats safely, handle decimals, reject invalid states, stop when value > 0.
- **Clean separation of concerns**:
  - `internet_bot.py` handles browser automation and data retrieval
  - `main.py` handles business logic (thresholds, deltas, messaging)
- **Readable “delta” logic**: compute `delta = measured - promised`, then use `delta >= 0` booleans to drive branching.
- **Formatting output**: `+.2f` formatting for signed deltas (positive/negative) and consistent summaries.
- **Environment variables**: loading secrets (`X_EMAIL`, `X_PASSWORD`) from `.env` instead of hardcoding.
- **Git hygiene**: adding Selenium profile folders to `.gitignore` to avoid committing personal browser data.


## ⚠️ Challenges

- **Speedtest UI timing**: values are not immediately numeric and can stay blank/dashes longer than expected.
- **Stability of locators**: UI selectors can be brittle across page updates (need resilient CSS selectors).
- **X/Twitter login friction**: automation triggers “unusual login activity” / anti-bot checks, blocking scripted login.
- **Tweet editor complexity**: the tweet box is nested in a rich text editor, and requires the right element (`data-testid`) to send keys reliably.


## ✅ Solutions / Insights

 **Built a `read_speed()` helper** that:
  - waits for the element to be visible
  - polls until the text becomes a valid number
  - enforces a hard timeout to avoid infinite loops
- **Returned floats** from `read_speed()` so downstream math is trivial (no repeated parsing in `main.py`).
- **Used `delta` everywhere** (`measured - promised`) and derived booleans (`delta >= 0`) to simplify branching.
- **Improved console UX** with status messages, checkmarks, and a clean “INTERNET SPEED SUMMARY” block.
- **Protected secrets + local state**:
  - moved credentials into `.env`
  - ignored profile folders via `.gitignore`
- **Reality check learned**: some websites (X) aggressively detect automation; Selenium flows can fail even if the code is correct.

## 📂 Project Structure

```text
day_51/
├── main.py
├── config.py
├── internet_bot.py
└── test_day_51.py
```

## 🏗 Architecture

```mermaid
flowchart TD
    A([Start]) --> B[Launch Selenium WebDriver]
    B --> C[Open speedtest.net]
    C --> D{Cookie popup?}
    D -->|Yes| E[Reject cookies]
    D -->|No| F[Continue]
    E --> F[Click GO]
    F --> G[Wait + poll Download value until numeric]
    G --> H[Wait + poll Upload value until numeric]
    H --> I[Compute deltas vs promised thresholds]
    I --> J{Both OK?}
    J -->|Yes| K[Print All good summary]
    J -->|No| L[Build complaint text]
    L --> M[Attempt X login + compose tweet]
    M --> N[Post tweet -if allowed-)]
    K --> O[Quit driver]
    N --> O[Quit driver]
    O --> P([End])
```

## 🎯 Next Steps

- **Make X step optional + resilient:**
  - ask confirmation `y/n` before attempting to post
  - detect “unusual activity” screens and bail with a clear message
- **Store a screenshot on failure** (login blocked / element not found) for easier debugging.
- **More robust selectors:**
  - centralize selectors in `config.py`
  - prefer `data-testid` when available over deep XPaths
- **Improve `read_speed()` validation:**
  - accept commas if locale uses `,` for decimals
  - log the last seen raw text on timeout
- **Refactor message formatting** into a helper that returns a summary + complaint string.
- **Capstone mindset for Day 53**: build a “deeper” version (better UX, validation, logging) without going full production.

---
[![prev_day](https://img.shields.io/badge/⬅️_Day_50-grey?style=for-the-badge)](day_50.md) [![next_day](https://img.shields.io/badge/Day_52_➡️-grey?style=for-the-badge)](day_52.md)
