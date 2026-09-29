from selenium import webdriver
from selenium.webdriver.common.by import By


def test_valid_login():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        username_box = driver.find_element(By.ID, "user-name")
        username_box.send_keys("standard_user")

        password_box = driver.find_element(By.ID, "password")
        password_box.send_keys("secret_sauce")

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # Verify login by checking the Products page URL
        assert "inventory.html" in driver.current_url

    finally:
        driver.quit()