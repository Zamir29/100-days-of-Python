from selenium import webdriver

def main():
    # Keep Chrome browser open after program finishes
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.amazon.com")

    # driver.close() # Close a tab
    # driver.quit() # Quit the entire program

if __name__ == '__main__':
    main()
