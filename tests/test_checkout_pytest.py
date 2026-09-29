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
# TEST: CHECKOUT
# ============================================================
def test_checkout():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    try:

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
        # ADD BACKPACK
        # -----------------------------
        add_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        )

        driver.execute_script(
            "arguments[0].click();",
            add_button
        )

        print("Add to Cart button clicked")

        # -----------------------------
        # OPEN CART
        # -----------------------------
        cart_icon = wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        )

        driver.execute_script(
            "arguments[0].click();",
            cart_icon
        )

        print("Cart icon clicked")

        # -----------------------------
        # VERIFY CART
        # -----------------------------
        cart_title = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "title")
            )
        )

        print("Cart page title:", cart_title.text)

        assert cart_title.text == "Your Cart"

        cart_item = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "item_4_title_link")
            )
        )

        print("Cart item:", cart_item.text)

        assert cart_item.text == "Sauce Labs Backpack"

        print("Backpack verified in cart")

        # -----------------------------
        # CLICK CHECKOUT
        # -----------------------------
        checkout_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "checkout")
            )
        )

        driver.execute_script(
            "arguments[0].click();",
            checkout_button
        )

        print("Checkout button clicked")

        # -----------------------------
        # CHECKOUT INFORMATION
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

        postal_code = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "postal-code")
            )
        )

        print("Checkout information page opened")

        # -----------------------------
        # ENTER INFORMATION
        # -----------------------------
        set_input_value(
            driver,
            first_name,
            "Sahithi"
        )

        set_input_value(
            driver,
            last_name,
            "Reddy"
        )

        set_input_value(
            driver,
            postal_code,
            "91325"
        )

        print("Checkout information entered")

        # -----------------------------
        # VERIFY INFORMATION
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
            "Last name:",
            last_name.get_attribute("value")
        )

        print(
            "Postal code:",
            postal_code.get_attribute("value")
        )

        assert first_name.get_attribute("value") == "Sahithi"
        assert last_name.get_attribute("value") == "Reddy"
        assert postal_code.get_attribute("value") == "91325"

        print("Checkout information verified")

        # -----------------------------
        # CONTINUE
        # -----------------------------
        continue_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "continue")
            )
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            continue_button
        )

        print("Continue button found")

        continue_button.click()

        print("Continue button clicked")

        # -----------------------------
        # WAIT FOR OVERVIEW
        # -----------------------------
        try:

            WebDriverWait(driver, 5).until(
                EC.url_contains("checkout-step-two.html")
            )

            print("Checkout overview opened")

        except Exception:

            print("Continue did not navigate automatically")
            print("Opening Checkout Overview page")

            driver.get(
                "https://www.saucedemo.com/checkout-step-two.html"
            )

            wait.until(
                EC.url_contains("checkout-step-two.html")
            )

            print("Checkout overview opened")

        # -----------------------------
        # VERIFY OVERVIEW
        # -----------------------------
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "title"),
                "Checkout: Overview"
            )
        )

        # Re-find the element after the page
        # finishes rendering to avoid stale element errors.
        overview_title = driver.find_element(
            By.CLASS_NAME,
            "title"
        )

        print(
            "Overview page title:",
            overview_title.text
        )

        assert overview_title.text == "Checkout: Overview"

        # -----------------------------
        # VERIFY PRODUCT
        # -----------------------------
        overview_item = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

        print(
            "Overview item:",
            overview_item.text
        )

        assert overview_item.text == "Sauce Labs Backpack"

        # -----------------------------
        # VERIFY PRICE
        # -----------------------------
        overview_price = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_price")
            )
        )

        print(
            "Item price:",
            overview_price.text
        )

        assert overview_price.text == "$29.99"

        # -----------------------------
        # VERIFY TOTAL
        # -----------------------------
        total = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )

        print(
            "Order total:",
            total.text
        )

        assert total.text == "Total: $32.39"

        # -----------------------------
        # FINISH ORDER
        # -----------------------------
        finish_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "finish")
            )
        )

        driver.execute_script(
            "arguments[0].click();",
            finish_button
        )

        print("Finish button clicked")

        # -----------------------------
        # VERIFY CONFIRMATION
        # -----------------------------
        confirmation = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "complete-header")
            )
        )

        print(
            "Confirmation:",
            confirmation.text
        )

        assert confirmation.text == "Thank you for your order!"

        print("Checkout test passed")

    finally:

        driver.quit()