from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_products():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Open SauceDemo
        driver.get("https://www.saucedemo.com/")

        # -------------------------
        # LOGIN
        # -------------------------

        username_box = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_box.send_keys("standard_user")

        password_box = wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_box.send_keys("secret_sauce")

        login_button = wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()

        # -------------------------
        # PRODUCT NAME
        # -------------------------

        product_name = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        ).text

        print("Product name:", product_name)

        assert product_name != ""

        # -------------------------
        # PRODUCT PRICE
        # -------------------------

        product_price = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_price")
            )
        ).text

        print("Product price:", product_price)

        assert product_price.startswith("$")

        # -------------------------
        # ADD TO CART
        # -------------------------

        add_to_cart = wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "btn_inventory")
            )
        )

        add_to_cart.click()

        print("Backpack added to cart")

        # -------------------------
        # OPEN CART
        # -------------------------

        cart_icon = wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        )

        cart_icon.click()

        print("Cart page opened")

        # -------------------------
        # VERIFY CART ITEM
        # -------------------------

        cart_item = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        ).text

        print("Cart item:", cart_item)

        assert cart_item == "Sauce Labs Backpack"

        print("Products test passed")

    finally:
        driver.quit()