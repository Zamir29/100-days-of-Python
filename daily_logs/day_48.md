# Day 48 — Selenium WebDriver: Browser Automation & Advanced Web Scraping <!-- omit in toc -->

[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2048-Open%20Folder-blue)](../day_48/main.py)  

| **Scope** | **Description** |
|:---------:|:----------------|
|   Goal    | Learn how Selenium WebDriver automates a real browser to interact with websites (type, click, scroll) beyond what BeautifulSoup can do. Use it to run repeatable “human-like” flows with Python.          |
|   Steps   | Install Selenium and set up a WebDriver (Chrome/Safari) to launch a browser and open pages via Python. Practice locating elements and performing actions like typing, clicking, and scrolling.         |
|   Stack   | `Python`, `Selenium`, `WebDriver` (ChromeDriver/SafariDriver), `VS Code`/`PyCharm`, `Chrome` or `Safari`.         |

## 📘 Table of contents <!-- omit in toc -->

- [🧠 Concepts Learned](#-concepts-learned)
- [⚠️ Challenges](#️-challenges)
- [✅ Solutions / Insights](#-solutions--insights)
- [📂 Project Structure](#-project-structure)
- [🏗 Architecture](#-architecture)
- [🎯 Next Steps](#-next-steps)

---

## 🧠 Concepts Learned

- **Selenium WebDriver basics**: launching Chrome, navigating pages, locating elements, clicking, typing. 
- **Dynamic pages**: why websites can “change under you” (JS re-renders DOM), causing flaky selectors. 
- **Waiting properly**: using `WebDriverWait` + `expected_conditions` instead of guessing with `sleep()`. 
- **Robust automation patterns**:
  - Re-find elements instead of storing them when the DOM updates. 
  - Handle popups/banners that reappear and break flows. 
  - Use retries for unstable reads (`safe_text`) and clicks.
- **Automation logic**: loop that clicks continuously + periodic decision-making (upgrades/products) + adaptive timer based on CPS and prices.

## ⚠️ Challenges

- Consent banner kept reappearing and breaking the run (`ElementNotInteractable`, then `StaleElementReference`). 
- Shimmers occasionally escaped clicking. 
- DOM re-renders caused stale element crashes for products, upgrades, and CPS reads. 
- Parsing “human formatted” numbers like `1.193 million` into real numeric values. 
- Timer logic broke when reads returned empty strings (`IndexError`).

## ✅ Solutions / Insights

- Built a **banner killer** (`close_banner_if_present`) with retry + JS click + periodic checks. 
- Fixed shimmer capture by selecting `.shimmer` and re-checking inside the loop. 
- Eliminated staleness by:
  - Re-finding upgrades each iteration before clicking.
  - Re-finding products by id during purchase loops. 
  - Using `safe_text()` with retries to read CPS/cookies safely.
- Implemented adaptive recheck time:
  - `wait_seconds = (price - cookies_now) / cps` clamped to stay responsive.
- Result: stable automation that hit ~90 CPS in 5 minutes.

## 📂 Project Structure

```text
day_48/
├── config.py
├── cookie_clicker.py
├── interaction.py
└── main.py
```

## 🏗 Architecture

```mermaid
flowchart TD
    A([Start]) --> B[Launch Chrome WebDriver]
    B --> C[Open Cookie Clicker URL]
    C --> D[Wait for language prompt]
    D --> E[Click EN]
    E --> F[Close banner if present]
    F --> G[Wait for Big Cookie clickable]
    G --> H[Init timers: end, next_check, next_banner_check]

    H --> I{Time < end?}
    I -->|Yes| J[Click Big Cookie]
    J --> K[Click any shimmers]
    K --> L{Time >= next_banner_check?}
    L -->|Yes| M[Close banner if present]
    M --> N[Set next_banner_check = now + 2s]
    L -->|No| O{Time >= next_check?}
    N --> O

    O -->|No| I

    O -->|Yes| P[Buy enabled upgrades]
    P --> Q[Buy unlocked products\nmost expensive to cheapest]
    Q --> R[Read CPS safely]
    R --> S{CPS valid?}
    S -->|No| T[Set next_check = now + 0.5s]
    T --> I

    S -->|Yes| U[Read cookies safely]
    U --> V{Cookies valid?}
    V -->|No| T

    V -->|Yes| W[Refresh unlocked products list]
    W --> X{Any unlocked products?}
    X -->|No| T

    X -->|Yes| Y[Pick best unlocked product]
    Y --> Z[Read best price]
    Z --> AA[Compute missing cookies]
    AA --> AB[Compute wait_seconds\nclamp 0.2 to 5.0]
    AB --> AC[Set next_check = now + wait_seconds]
    AC --> I

    I -->|No| AD([Stop])


```

## 🎯 Next Steps

- Day 49: keep the “Angela baseline” + add **one small upgrade** (e.g., lightweight stats logging per check).

Optional side quest: move your helpers (`safe_text`, `close_banner_if_present`, `parse_human_number`) into a tiny `utils.py` for reuse across Selenium scripts. 

---
[![prev_day](https://img.shields.io/badge/⬅️_Day_47-grey?style=for-the-badge)](day_47.md) [![next_day](https://img.shields.io/badge/Day_49_➡️-grey?style=for-the-badge)](day_49.md)
