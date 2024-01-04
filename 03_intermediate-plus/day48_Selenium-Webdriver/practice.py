from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)

    # # Amazon Price checker
    # driver.get("https://www.amazon.com/Audio-Technica-AT-LP60X-BK-Belt-Drive-Hi-Fidelity-Anti-Resonance/dp/B07N3XJ66N/")
    # price_dollar = driver.find_element(By.CLASS_NAME, 'a-price-whole')
    # price_cents = driver.find_element(By.CLASS_NAME, 'a-price-fraction')
    # print(f"The price is {price_dollar.text}.{price_cents.text}")

    # Python.org check
    driver.get("https://www.python.org")

    # # Practice
    # search_bar = driver.find_element(By.NAME, value="q")
    # print(search_bar.get_attribute("placeholder"))
    # button = driver.find_element(By.ID, value="submit")
    # print(button.size)
    # documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
    # print(documentation_link.text)
    # bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
    # print(bug_link.get_attribute("href"))

    # Challenge #1
    upcoming_events_menu = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
    upcoming_events = []

    for event in upcoming_events_menu.find_elements(By.CSS_SELECTOR, value="li"):
        event_date = event.find_element(By.TAG_NAME, value="time").get_attribute("datetime").split("T")[0]
        event_name = event.find_element(By.TAG_NAME, value="a").text

        upcoming_events.append({"time": event_date, "name": event_name})

    print(upcoming_events)

    # driver.close()
    driver.quit()
