from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def make_driver():
    # Keep Chrome browser open after program finishes
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    # Start instance of Chrome
    return webdriver.Chrome(options=chrome_options)

def interaction_kickstart():
    # Start instance of Chrome
    driver = make_driver()

    # Go to website
    website_url = "https://en.wikipedia.org/wiki/Main_Page"
    driver.get(website_url)

    # # Get the statistics and the articles count
    # statistics = driver.find_element(By.CSS_SELECTOR, value="div#articlecount")
    # articles_count = statistics.find_elements(By.TAG_NAME, value="a")[1]
    #
    # print(articles_count.text)

    # # Use the text in a link to target and to click
    # all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
    # all_portals.click()

    # Find the "Search" <input> by NAME
    search = driver.find_element(By.NAME, value="search")

    # Sending keyboard input to Selenium
    search.send_keys("Python", Keys.RETURN)

    # # Alternative, click Search button
    # button_search = driver.find_element(By.CSS_SELECTOR, value="button.cdx-search-input__end-button")
    # button_search.click()



    # ------- Code above
    # driver.quit()  # Quit the instance

def fill_form():
    # Start instance of Chrome
    driver = make_driver()

    # Go to website
    website_url = "http://secure-retreat-92358.herokuapp.com/"
    driver.get(website_url)

    # Fill Form
    form = driver.find_element(By.TAG_NAME, value="form")

    fname = form.find_element(By.NAME, value="fName")
    fname.send_keys("Costantino")

    lname = form.find_element(By.NAME, value="lName")
    lname.send_keys("Imperatore")

    email = form.find_element(By.NAME, value="email")
    email.send_keys("costantino.imperatore@roma.com")

    # Submit form
    submit_button = form.find_element(By.CSS_SELECTOR, value="button[type='submit']")
    submit_button.click()

    # ------- Code above
    # driver.quit()  # Quit the instance

def main():
    fill_form()

if __name__ == "__main__":
    main()