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
    statistics = driver.find_elements(By.CSS_SELECTOR, value="div#articlecount ul li a")
    articles_count = statistics[1].text
    print(articles_count)

    driver.quit()  # Quit the instance

if __name__ == "__main__":
    main()