from selenium import webdriver
from selenium.webdriver.common.by import By
from config import (
    AMAZON_URL,
)

def learn_selenium():
    # Keep Chrome browser open after program finishes
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    # Start instance of Chrome
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(AMAZON_URL)
    # # Use locators as explained in https://www.selenium.dev/documentation/webdriver/elements/locators/
    # price_eur = driver.find_element(By.CLASS_NAME, value="a-price-whole")
    # price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
    #
    # print(f"The price is {price_eur.text}.{price_cents.text}")

    # # Search by name on Python.org
    driver.get("https://www.python.org/")
    # search_bar = driver.find_element(By.NAME, value="q")
    # button = driver.find_element(By.ID, value="submit")
    # print(button.size)
    # documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
    # print(documentation_link.text)

    bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

    print(bug_link.text)

    # driver.close() # Close a tab
    # driver.quit() # Quit the entire program

def extract_events_challenge():
    # Keep Chrome browser open after program finishes
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    # Start instance of Chrome
    driver = webdriver.Chrome(options=chrome_options)

    # Open Python org page
    driver.get("https://www.python.org/")


    # Get the list of events
    events_list = driver.find_elements(By.CSS_SELECTOR, value='.event-widget ul.menu li')

    # Build dictionary with enumerate to extract the index
    events = {}
    for i,event in enumerate(events_list):
        date = event.find_element(By.TAG_NAME, value='time').text
        title = event.find_element(By.TAG_NAME, value='a').text
        events[i] = {"time": date, "name": title}

    print(events)

    driver.quit() # Quit the entire program

def main():
    extract_events_challenge()
if __name__ == '__main__':
    main()
