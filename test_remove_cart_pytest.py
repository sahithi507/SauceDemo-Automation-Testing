from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_remove_from_cart():

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

        print("Login successful")

        # -----------------------------
        # ADD BACKPACK
        # -----------------------------
        add_button = wait.until(
            EC.presence_of_element_located(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        )

        # Use JavaScript click
        driver.execute_script(
            "arguments[0].click();",
            add_button
        )

        print("Backpack added to cart")

        # -----------------------------
        # OPEN CART
        # -----------------------------
        cart_icon = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        )

        # Use JavaScript click
        driver.execute_script(
            "arguments[0].click();",
            cart_icon
        )

        print("Cart icon clicked")

        # -----------------------------
        # VERIFY CART PAGE
        # -----------------------------
        wait.until(
            EC.url_contains("cart.html")
        )

        print("Cart page opened")

        # -----------------------------
        # VERIFY CART TITLE
        # -----------------------------
        cart_title = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "title")
            )
        )

        print("Cart page title:", cart_title.text)

        assert cart_title.text == "Your Cart"

        # -----------------------------
        # VERIFY BACKPACK
        # -----------------------------
        cart_item = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "item_4_title_link")
            )
        )

        print("Cart item:", cart_item.text)

        assert cart_item.text == "Sauce Labs Backpack"

        print("Backpack verified in cart")

        # -----------------------------
        # REMOVE BACKPACK
        # -----------------------------
        remove_button = wait.until(
            EC.presence_of_element_located(
                (By.ID, "remove-sauce-labs-backpack")
            )
        )

        print("Remove button found")

        # JavaScript click
        driver.execute_script(
            "arguments[0].click();",
            remove_button
        )

        print("Remove button clicked")

        # -----------------------------
        # VERIFY CART EMPTY
        # -----------------------------
        wait.until(
            lambda d: len(
                d.find_elements(
                    By.ID,
                    "item_4_title_link"
                )
            ) == 0
        )

        print("Backpack removed from cart")

        # -----------------------------
        # VERIFY BADGE GONE
        # -----------------------------
        wait.until(
            lambda d: len(
                d.find_elements(
                    By.CLASS_NAME,
                    "shopping_cart_badge"
                )
            ) == 0
        )

        print("Cart is empty")
        print("Remove from cart test passed")

    finally:
        driver.quit()