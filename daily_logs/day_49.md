# Day 49 — Automating Gym Class Bookings with Selenium (Snack & Lift) <!-- omit in toc -->

[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2049-Open%20Folder-blue)](../day_49/main.py)  

| **Scope** | **Description** |
|:---------:|:----------------|
|   Goal    | Automate a real browser with Selenium to log in and book gym classes on the Snack & Lift site. Practice reliable element waits, handling dynamic UI states (book/full/waitlist), and building resilient automation.          |
|   Steps   | Set up Selenium with a persistent Chrome profile, automate login, then iterate through class listings to book or join waitlists based on button state. Add retry + validation logic to handle simulated network/time changes and confirm bookings in “My Bookings”.         |
|   Stack   | `Python`, `Selenium WebDriver`, Google Chrome + ChromeDriver (persistent profile), `WebDriverWait`/`Expected Conditions`. Local Snack & Lift practice website (browser storage / `IndexedDB`).         |

## 📘 Table of contents <!-- omit in toc -->

- [🧠 Concepts Learned](#-concepts-learned)
- [⚠️ Challenges](#️-challenges)
- [✅ Solutions / Insights](#-solutions--insights)
- [📂 Project Structure](#-project-structure)
- [🏗 Architecture](#-architecture)
- [🎯 Next Steps](#-next-steps)

---

## 🧠 Concepts Learned

- **Persistent Chrome session** with `--user-data-dir=chrome_profile` + `detach=True` to keep cookies/session between runs (and why you must *quit Chrome manually* before rerunning).
- **Explicit waits > sleep**: using `WebDriverWait` + `expected_conditions` (`presence_of_element_located`, `visibility_of_element_located`, `element_to_be_clickable`) to avoid flaky automation.
- **UI-state driven automation**: reading `button.text` to decide behavior (`Booked`, `Waitlisted`, `Book Class`, `Join Waitlist`).
- **Replacing if/elif chains with a rule dictionary**: mapping `status -> (message, should_click, counter_bucket, tag)` to scale better if the website adds new statuses.
- **Simple resilience pattern**: a `retry(func, retries=7)` wrapper that retries Selenium actions when timeouts happen (simulated network failures).
- **Verification step**: navigating to **My Bookings**, parsing booking cards, and validating “expected vs found” bookings.
- **Git hygiene for automation projects**: adding `chrome_profile/` to `.gitignore`, removing tracked artifacts with `git rm -r --cached`, and checking history to ensure nothing remains tracked.


## ⚠️ Challenges

- **Chrome profile accidentally tracked** in git (risk: huge folder + session artifacts + noisy repo).
- **Git push confusion on a new machine**: `main` had no upstream branch, so `git push` failed until upstream was set.
- **Selenium gotchas**:
  - Runs failing when Chrome was still open (because of `detach=True`).
  - Network simulation causing random `TimeoutException` during login/booking/navigation.
  - Small page-id differences can break waits (`my-bookings-page` vs `my-booking-page`).
- **Tooling friction**:
  - PyCharm warning like “Missing return statement on some paths” (static analyzer being extra dramatic).
  - Terminal glitches after installing Starship (especially when resizing the terminal window).

## ✅ Solutions / Insights

- **Git cleanup fix (the right way):**
  - Added `chrome_profile/` to `.gitignore`.
  - Removed it from tracking: `git rm -r --cached chrome_profile`.
  - Verified it’s gone:
    - `git ls-files | grep -i chrome_profile` (no output ✅)
    - `git rev-list --objects --all | grep -i chrome_profile` (no output ✅)
- **Upstream push fix:**
  - First push after new setup: `git push --set-upstream origin main`.
  - Optional convenience: `git config --global push.autoSetupRemote true`.
- **Selenium reliability upgrade:**
  - Kept `login()` as a single responsibility flow and made it robust with explicit waits.
  - Used a **rules dictionary** to keep booking logic readable + scalable.
  - Added a `retry()` wrapper around operations that can fail due to network simulation (timeouts).
- **Verification mindset:**
  - Booking automation is not “done” after clicking — confirm via UI state or a second source (“My Bookings” page) to ensure the action truly worked.


## 📂 Project Structure

```text
day_49/
├── main.py
├── config.py
```

## 🏗 Architecture

```mermaid
flowchart TD
    A([Start]) --> B[make_driver() with persistent chrome_profile]
    B --> C[Open Gym URL]
    C --> D[login()]

    D --> E[Open Schedule Page]
    E --> F[Find all class cards]
    F --> G{Is Tue/Thu AND 6:00 PM?}

    G -->|No| F
    G -->|Yes| H[Read booking button.text -> status]
    H --> I[Lookup status in rules dict]
    I --> J{should_click?}

    J -->|No| K[Count + log + store processed class]
    J -->|Yes| L[Click booking button]
    L --> M[Wait a moment / UI updates]
    M --> K

    K --> F

    F --> N[Compute totals]
    N --> O[Go to My Bookings page]
    O --> P[Find booking cards]
    P --> Q[Verify Tue/Thu 6pm bookings count]
    Q --> R{expected == found?}
    R -->|Yes| S([SUCCESS ✅])
    R -->|No| T([MISMATCH ❌])
```

## 🎯 Next Steps

🎯 Next Steps

- Wrap the most failure-prone actions with `retry()`:
  - `retry(lambda: login(driver, wait), description="login")`
  - `retry(lambda: click_and_confirm(button), description="booking")` (confirm by waiting for button text to change)
  - `retry(get_my_bookings, description="my bookings navigation")`
- Improve booking confirmation:
  - After click, wait until button text becomes `"Booked"` or `"Waitlisted"` (instead of fixed `sleep`).
- Refactor for readability:
  - Extract small helpers: `is_target_slot(day_title, time_text)`, `handle_status(status, button, class_info)`.
- Add better debug logging:
  - Print the status that was encountered when it’s unknown.
- Optional: add a “dry run” mode to print what would be booked without clicking.

---
[![prev_day](https://img.shields.io/badge/⬅️_Day_48-grey?style=for-the-badge)](day_48.md) [![next_day](https://img.shields.io/badge/Day_50_➡️-grey?style=for-the-badge)](day_50.md)
