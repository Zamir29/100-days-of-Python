# Day 50 — Day 50 - Auto Tinder Swiping Bot <!-- omit in toc -->

[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2050-Open%20Folder-blue)](../day_50/main.py)  

| **Scope** | **Description** |
|:---------:|:----------------|
|   Goal    | Build a Selenium automation script that logs into Tinder on the web, handles popups/permissions, and performs automated swipes in a controlled loop.          |
|   Steps   | Set up Selenium + WebDriver, automate the login flow, then add reliable waits and popup handling while looping swipes until a limit (time or count) is reached.         |
|   Stack   | `Python`, `Selenium WebDriver`, `Chrome` (or `Safari`) + `WebDriver`/`Selenium Manager`, `VS Code`/`PyCharm`.         |

## 📘 Table of contents <!-- omit in toc -->

- [🧠 Concepts Learned](#-concepts-learned)
- [⚠️ Challenges](#️-challenges)
- [✅ Solutions / Insights](#-solutions--insights)
- [📂 Project Structure](#-project-structure)
- [🏗 Architecture](#-architecture)
- [🎯 Next Steps](#-next-steps)

---

## 🧠 Concepts Learned

- How Selenium handles **multiple windows** (Facebook login popup) using `driver.current_window_handle` + `driver.window_handles` and `switch_to.window()`.
- Why `WebDriverWait` + `expected_conditions` beats `sleep()` for **dynamic UIs** (buttons that appear late / change state).
- Practical exception handling for UI automation: `TimeoutException` (waits), `ElementClickInterceptedException` (overlays), and “try/ignore if not present” popups.
- Git workflow upgrades: `git switch -c`, upstream tracking, `commit --amend` + `push --force-with-lease`, merge with `--no-ff`, and bulk cleanup of merged branches (local + remote).

## ⚠️ Challenges

- Unstable DOM + overlays: “clickable” elements still getting blocked by popups (matches, permissions, cookies).
- Brittle selectors (long XPaths) and small typos causing silent failures; waits changed failure mode from `NoSuchElementException` to `TimeoutException`.
- Git maintenance: lots of old branches created clutter and made navigation/error recovery harder.

## ✅ Solutions / Insights

- Replaced most `sleep()` calls with **explicit waits** and created tiny helpers (`wait_click`, `wait_find`) to keep the code readable.
- Waited for the Facebook popup using `number_of_windows_to_be(2)` and selected the non-base handle instead of relying on index order.
- Added **defensive popup handling** with `try/except TimeoutException` so optional modals don’t crash the script.
- Cleaned Git history and workflow: corrected a pushed commit message safely (`--force-with-lease`), merged Day 50 into `main`, then deleted merged branches in bulk (local + remote) and pruned remotes.

## 📂 Project Structure

```text
day_50/
├── main.py
├── config.py
```

## 🏗 Architecture

```mermaid
flowchart TD
    A([Start]) --> B[Open tinder.com]
    B --> C[Click Log In]
    C --> D[Click Log in with Facebook]
    D --> E{Popup window opened?}
    E -- Yes --> F[Switch to FB window]
    F --> G[Enter email + password]
    G --> H[Submit (ENTER)]
    H --> I[Switch back to Tinder window]
    E -- No --> D

    I --> J[Handle optional popups<br/>(location / notifications / cookies)]
    J --> K[Loop up to N swipes]
    K --> L[Wait & click Like button]
    L --> M{Click intercepted?}
    M -- No --> K
    M -- Yes --> N[Try close match / overlay]
    N --> K

    K --> O([Quit driver / End])
```

## 🎯 Next Steps

- Reduce XPath fragility: prefer `By.ID` / stable CSS selectors where possible; centralize selectors in constants.
- Replace the last remaining `sleep()` in the swipe loop with waits + a small retry/backoff strategy.
- Add lightweight observability: swipe counter logs, screenshot on failure, and an early exit when daily swipe limit is reached.
  (Optional) Refactor into small functions: 'login()', `handle_popups()`, `swipe_loop()` for clarity and easier debugging.

---
[![prev_day](https://img.shields.io/badge/⬅️_Day_49-grey?style=for-the-badge)](day_49.md) [![next_day](https://img.shields.io/badge/Day_51_➡️-grey?style=for-the-badge)](day_51.md)
