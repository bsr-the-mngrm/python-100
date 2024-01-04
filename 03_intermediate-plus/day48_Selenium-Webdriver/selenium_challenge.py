from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to Wikipedia
    driver.get("https://secure-retreat-92358.herokuapp.com/")

    # Type in first name
    fName_input = driver.find_element(By.NAME, "fName")
    fName_input.send_keys("John")

    # Type in last name
    lName_input = driver.find_element(By.NAME, "lName")
    lName_input.send_keys("Doe")

    # Type in email
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("john.doe@example.com")

    # Click on sign up
    signUp_btn = driver.find_element(By.CLASS_NAME, "btn-block")
    signUp_btn.click()
