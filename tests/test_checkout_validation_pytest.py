from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ============================================================
# HELPER: SET INPUT VALUE
# ============================================================
def set_input_value(driver, element, value):

    driver.execute_script(
        """
        const input = arguments[0];
        const value = arguments[1];

        const setter = Object.getOwnPropertyDescriptor(
            window.HTMLInputElement.prototype,
            "value"
        ).set;

        setter.call(input, value);

        input.dispatchEvent(
            new Event("input", { bubbles: true })
        );

        input.dispatchEvent(
            new Event("change", { bubbles: true })
        );

        input.dispatchEvent(
            new Event("blur", { bubbles: true })
        );
        """,
        element,
        value
    )


# ============================================================
# HELPER: OPEN CHECKOUT INFORMATION PAGE
# ============================================================
def open_checkout_page(driver, wait):

    # -----------------------------
    # OPEN SAUCEDEMO
    # -----------------------------
    driver.get("https://www.saucedemo.com/")

    # -----------------------------
    # LOGIN
    # -----------------------------
    username = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    )

    username.send_keys("standard_user")

    password = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "password")
        )
    )

    password.send_keys("secret_sauce")

    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "login-button")
        )
    )

    login_button.click()

    wait.until(
        EC.url_contains("inventory.html")
    )

    print("Login successful")

    # -----------------------------
    # OPEN CHECKOUT INFORMATION PAGE
    # -----------------------------
    driver.get(
        "https://www.saucedemo.com/checkout-step-one.html"
    )

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "first-name")
        )
    )

    print("Checkout page opened")


# ============================================================
# HELPER: GET ERROR MESSAGE
# ============================================================
def get_error_message(driver, wait):

    error = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    print("Error message:", error.text)

    return error.text


# ============================================================
# TEST 1: ALL FIELDS EMPTY
# ============================================================
def test_checkout_empty_fields():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    try:

        open_checkout_page(driver, wait)

        # -----------------------------
        # CLICK CONTINUE
        # -----------------------------
        continue_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "continue")
            )
        )

        driver.execute_script(
            "arguments[0].click();",
            continue_button
        )

        print("Continue button clicked")

        # -----------------------------
        # VERIFY ERROR
        # -----------------------------
        error_message = get_error_message(
            driver,
            wait
        )

        assert error_message == (
            "Error: First Name is required"
        )

        print("Empty fields validation passed")

    finally:

        driver.quit()


# ============================================================
# TEST 2: LAST NAME MISSING
# ============================================================
def test_checkout_missing_last_name():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    try:

        open_checkout_page(driver, wait)

        # -----------------------------
        # FIRST NAME
        # -----------------------------
        first_name = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        )

        set_input_value(
            driver,
            first_name,
            "Sahithi"
        )

        # -----------------------------
        # POSTAL CODE
        # -----------------------------
        postal_code = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "postal-code")
            )
        )

        set_input_value(
            driver,
            postal_code,
            "91325"
        )

        print("First name and postal code entered")

        # -----------------------------
        # VERIFY VALUES
        # -----------------------------
        first_name = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        )

        postal_code = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "postal-code")
            )
        )

        print(
            "First name:",
            first_name.get_attribute("value")
        )

        print(
            "Postal code:",
            postal_code.get_attribute("value")
        )

        assert first_name.get_attribute("value") == "Sahithi"
        assert postal_code.get_attribute("value") == "91325"

        # Last name intentionally remains empty

        # -----------------------------
        # CLICK CONTINUE
        # -----------------------------
        continue_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "continue")
            )
        )

        driver.execute_script(
            "arguments[0].click();",
            continue_button
        )

        print("Continue button clicked")

        # -----------------------------
        # VERIFY ERROR
        # -----------------------------
        error_message = get_error_message(
            driver,
            wait
        )

        assert error_message == (
            "Error: Last Name is required"
        )

        print("Missing last name validation passed")

    finally:

        driver.quit()


# ============================================================
# TEST 3: POSTAL CODE MISSING
# ============================================================
def test_checkout_missing_postal_code():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    try:

        open_checkout_page(driver, wait)

        # -----------------------------
        # FIRST NAME
        # -----------------------------
        first_name = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        )

        set_input_value(
            driver,
            first_name,
            "Sahithi"
        )

        # -----------------------------
        # LAST NAME
        # -----------------------------
        last_name = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "last-name")
            )
        )

        set_input_value(
            driver,
            last_name,
            "Reddy"
        )

        print("First name and last name entered")

        # -----------------------------
        # VERIFY VALUES
        # -----------------------------
        first_name = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "first-name")
            )
        )

        last_name = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "last-name")
            )
        )

        print(
            "First name:",
            first_name.get_attribute("value")
        )

        print(
            "Last name:",
            last_name.get_attribute("value")
        )

        assert first_name.get_attribute("value") == "Sahithi"
        assert last_name.get_attribute("value") == "Reddy"

        # Postal code intentionally remains empty

        # -----------------------------
        # CLICK CONTINUE
        # -----------------------------
        continue_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "continue")
            )
        )

        driver.execute_script(
            "arguments[0].click();",
            continue_button
        )

        print("Continue button clicked")

        # -----------------------------
        # VERIFY ERROR
        # -----------------------------
        error_message = get_error_message(
            driver,
            wait
        )

        assert error_message == (
            "Error: Postal Code is required"
        )

        print("Missing postal code validation passed")

    finally:

        driver.quit()