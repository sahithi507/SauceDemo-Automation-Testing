from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_invalid_login():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:

        # -----------------------------
        # OPEN SAUCEDEMO
        # -----------------------------
        driver.get("https://www.saucedemo.com/")

        # -----------------------------
        # ENTER INVALID USERNAME
        # -----------------------------
        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        ).send_keys("wrong_user")

        # -----------------------------
        # ENTER INVALID PASSWORD
        # -----------------------------
        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "password")
            )
        ).send_keys("wrong_password")

        # -----------------------------
        # CLICK LOGIN
        # -----------------------------
        wait.until(
            EC.element_to_be_clickable(
                (By.ID, "login-button")
            )
        ).click()

        print("Invalid login attempted")

        # -----------------------------
        # VERIFY ERROR MESSAGE
        # -----------------------------
        error_message = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='error']")
            )
        )

        error_text = error_message.text

        print("Error message:", error_text)

        # -----------------------------
        # VERIFY LOGIN FAILED
        # -----------------------------
        assert "Username and password do not match" in error_text

        print("Invalid login test passed")

    finally:
        driver.quit()