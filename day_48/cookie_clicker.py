import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

MAX_TIME = 5 * 60 # 5 minuts

def make_driver():
    # Keep Chrome browser open after program finishes
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    # Return a driver
    return webdriver.Chrome(options=chrome_options)

def safe_text(driver, by, value, retries=5):
    for _ in range(retries):
        try:
            return driver.find_element(by, value).text
        except StaleElementReferenceException:
            time.sleep(0.05)
    return ""

def parse_human_number(s: str) -> float:
    s = s.lower().replace(",", "").strip()
    mult = {"million": 1e6, "billion": 1e9, "trillion": 1e12, "quadrillion": 1e15}

    parts = s.split()
    n = float(parts[0])
    if len(parts) > 1 and parts[1] in mult:
        n *= mult[parts[1]]
    return n

def main():

    # Start a driver of Chrome
    driver = make_driver()
    wait = WebDriverWait(driver, 10)

    # Go to website
    website_url = "https://ozh.github.io/cookieclicker/"
    driver.get(website_url)

    # Wait for DOM to build the languange prompt

    # In the language prompt pick english
    language_prompt = wait.until(
        EC.element_to_be_clickable((By.ID, "promptContentChangeLanguage"))
    )
    # Click the button EN
    language_prompt.find_element(By.ID, value="langSelect-EN").click()

    # If Cookie Banner is present, click it
    banners = driver.find_elements(By.CSS_SELECTOR, "a.cc_btn_accept_all")
    if banners:
        driver.execute_script("arguments[0].click();", banners[0])


    cookie_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#bigCookie"))
    )

    # Start timer and check time
    end = time.time() + MAX_TIME
    next_check = time.time()


    # Start clicking and the whole logic
    while time.time() < end:
        cookie_button.click()

        # Capture shimmers
        for s in driver.find_elements(By.CSS_SELECTOR, ".shimmer"):
            try:
                s.click()
            except:
                pass

        if time.time() >= next_check:
            store_section = driver.find_elements(By.CSS_SELECTOR, value="#products .product.unlocked")

            # Find the first enabled upgrade and click it
            while True:
                upgrade_box = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
                if not upgrade_box:
                    break
                try:
                    driver.execute_script("arguments[0].click();", upgrade_box[0])
                except StaleElementReferenceException:
                    continue

            # Take the list of items and click the enabled until they become disabled
            for item in reversed(store_section):
                item_id = item.get_attribute("id")  # e.g. "product7"
                while True:
                    item = driver.find_element(By.ID, item_id)  # refresh reference
                    if "enabled" not in item.get_attribute("class").split():
                        break
                    item.click()

            if not store_section:
                next_check = time.time() + 0.5
                continue

            # Check cookie per second
            cps_text = safe_text(driver, By.ID, "cookiesPerSecond")

            if ":" not in cps_text:
                next_check = time.time() + 0.5
                continue

            cps_value_text = cps_text.split(":")[1].strip()
            cps_value = parse_human_number(cps_value_text)

            # Current cookies (first line of #cookies)
            cookies_text = safe_text(driver, By.ID, "cookies").split("\n")[0].strip()
            cookies_now = parse_human_number(cookies_text)

            # Use the best item unlocked to calculate how much to wait before recheck
            best_unlocked = store_section[-1] if store_section else None
            if not best_unlocked:
                next_check = time.time() + 0.5
                continue

            # Check price of best unlocked
            price_text = best_unlocked.find_element(By.CLASS_NAME, value="price").text.strip()
            price_value = parse_human_number(price_text)

            # 5) Compute wait time until affordable (clamp so you don't miss upgrades)
            missing = max(0.0, price_value - cookies_now)
            wait_seconds = (missing / cps_value) if cps_value > 0 else 0.5
            wait_seconds = max(0.2, min(wait_seconds, 5.0))  # keep it responsive

            next_check = time.time() + wait_seconds

        pass

    # ------- Code above
    # driver.quit()  # Quit the instance

if __name__ == "__main__":
    main()