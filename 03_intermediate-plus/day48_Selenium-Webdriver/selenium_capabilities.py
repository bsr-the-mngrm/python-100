from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to Wikipedia
    driver.get("https://en.wikipedia.org/wiki/Main_Page")

    # Hone in an anchor tag using CSS selectors
    wikipedia_article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
    wikipedia_article_count.click()

    # Find element by Link Text
    all_portals = driver.find_element(By.LINK_TEXT, value="Bots")
    all_portals.click()

    # Find the "Search" <input> by Name
    search = driver.find_element(By.NAME, "search")

    # Sending keyboard input to Selenium
    search.send_keys("Python", Keys.ENTER)
