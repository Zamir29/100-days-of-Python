# Day 35 — Keys, Auth & Environment Variables
[![Open Project Folder](https://img.shields.io/badge/📁%20Day%2035-Open%20Folder-blue)](../day_35/main.py)

## 📘 Table of contents
* [🧠 Concepts Learned](#-concepts-learned)
* [⚠️ Challenges](#-challenges)
* [✅ Solutions / Insights](#-solutions--insights)
* [🎯 Next steps](#-next-steps)

---

## 🧠 Concepts Learned

### 🔐 API Authentication Fundamentals
- APIs often require secure tokens (API_KEY, AUTH_TOKEN, SID, …).
- Keys must never be hardcoded in code.
- URL parameters can include keys but must be protected when stored locally.

### 🌍 HTTP requests with real-world APIs
- Used `requests.get()` with correct parameters.
- Learned the difference between:
  - `response.json()`
  - `response.status_code`
  - `response.url` (*for debugging request formation*)

### ☁️ Weather API Forecast Logic
- OpenWeatherMap weather codes:  
Rain = < 700.  
Clear/Safe = >= 700.

- Extracting nested JSON like:  
`forecast["weather"][0]["id"]`

### 🔒 Environment Variables (Real Engineering)
- `.env` file is just a text file, not interpreted automatically.
- `os.getenv("KEY")` reads environment variables only if loaded into the process.
- Installed EnvFile plugin to load `.env` before Python runs.
- Configured PyCharm Run Configuration:
  - Script path → main.py
  - Enabled EnvFile
  - Added .env to active loaders
- Understood why .env is a local-dev convenience, not a production mechanism.

### 🧱 Cloud-Relevant Knowledge
- Environment variables behave the same in:
  - Azure Functions
  - AWS Lambda
  - GCP Cloud Run 
  - Docker containers

- `.env` → for local dev
- Cloud secret managers → for production

## ⚠️ Challenges

1. **API key returning 401 Unauthorized**  
Cause: Environment variable wasn’t loaded properly → appid=None.

2. **PyCharm not loading `.env` file**
   - .env was hidden (dotfile)
   - EnvFile plugin not enabled yet
   - Wrong “Script Path” (running folder instead of file)

3. **False PyCharm warnings**
   - `os.getenv(OWM_API_KEY)` without quotes
   - “Unresolved reference” where PyCharm expects a Python variable, not a string.

4. **Confusion about Run Configurations**
   - Why we need them
   - What PyCharm actually does when starting a program
   - Why .env must be explicitly attached

## ✅ Solutions / Insights
### ✔ Fixing API Key Problems
- Used correct string:  
`os.getenv("OWM_API_KEY")`
- Attached `.env` in Run Config → EnvFile loads it before runtime.

### ✔ Environment Handling
- Finally understood the hierarchy:  
`.env` → EnvFile plugin → injected into environment → Python sees variables

### ✔ Cleaner Umbrella Logic
- Implemented beginner-friendly + scalable version:  
`will_rain = any(code < 700 for code in fetch_forecast)`  
And understood Angela’s version and how yours differed.

### ✔ Debugging Trick
- `print(response.url)` to verify what parameters were _actually_ sent.

### ✔ Keyboard Efficiency
Learned essential PyCharm shortcuts, multi-cursors, fast editing, and navigation.

## 🎯 Next Steps
### Short-term
- Start Day 36 (Working with APIs using Timers & PythonAnywhere — but you’ll skip PA and do it your way).
- Write a small wrapper function to fetch & parse forecasts cleanly.
- Log Day 36 immediately after finishing the lesson.

### Medium-term
- Create shared config.py for reading env variables across projects.
- Start standardizing your Python folder structure:
```
/src
/config
/logs
/services
```
### Long-term
- Move from `.env` → **Azure KeyVault** or **GCP Secret Manager** for real deployments.
- Use `python-dotenv` for projects that don’t rely on PyCharm.