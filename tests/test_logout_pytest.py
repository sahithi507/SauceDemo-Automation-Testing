from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logout():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:
        # OPEN SAUCEDEMO
        driver.get("https://www.saucedemo.com/")

        # LOGIN
        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        ).send_keys("standard_user")

        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "password")
            )
        ).send_keys("secret_sauce")

        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "login-button")
            )
        ).click()

        wait.until(
            EC.url_contains("inventory.html")
        )

        print("Products page opened")

        # OPEN MENU
        menu_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "react-burger-menu-btn")
            )
        )

        driver.execute_script(
            "arguments[0].click();",
            menu_button
        )

        print("Menu button clicked")

        # WAIT FOR LOGOUT BUTTON TO EXIST
        logout_button = wait.until(
            EC.presence_of_element_located(
                (By.ID, "logout_sidebar_link")
            )
        )

        # CLICK LOGOUT WITH JAVASCRIPT
        driver.execute_script(
            "arguments[0].click();",
            logout_button
        )

        print("Logout button clicked")

        # VERIFY LOGIN PAGE
        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        )

        print("Returned to login page")
        print("Logout test passed")

    finally:
        driver.quit()