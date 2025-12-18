from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    # Keep Chrome browser open after program finishes
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    # Start instance of Chrome
    driver = webdriver.Chrome(options=chrome_options)

    # Go to website
    website_url = "https://en.wikipedia.org/wiki/Main_Page"
    driver.get(website_url)

    # Get the statistics and the articles count
    statistics = driver.find_element(By.CSS_SELECTOR, value="div#articlecount")
    articles_count = statistics.find_elements(By.TAG_NAME, value="a")[1].text

    print(articles_count)

    driver.quit()  # Quit the instance

if __name__ == "__main__":
    main()