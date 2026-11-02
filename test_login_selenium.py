import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


BASE_URL = "http://localhost:5000"


def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    return driver


def test_valid_login():
    driver = get_driver()
    try:
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys("student1")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("pass123")

        driver.find_element(By.ID, "login-btn").click()

        success = wait.until(EC.presence_of_element_located((By.ID, "success-msg")))
        print("Valid login test PASSED:", success.text)
    finally:
        driver.quit()


def test_invalid_login():
    driver = get_driver()
    try:
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys("wronguser")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("wrongpass")

        driver.find_element(By.ID, "login-btn").click()

        error = wait.until(EC.presence_of_element_located((By.ID, "error-msg")))
        print("Invalid login test PASSED:", error.text)
    finally:
        driver.quit()


if __name__ == "__main__":
    print("Running Selenium login tests...")
    test_valid_login()
    test_invalid_login()
    print("All Selenium tests done.")
