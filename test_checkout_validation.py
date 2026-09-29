from selenium import webdriver
from selenium.webdriver.common.by import By

# Open browser
driver = webdriver.Chrome()

# Open SauceDemo
driver.get("https://www.saucedemo.com/")

# -------------------------
# LOGIN
# -------------------------

username_box = driver.find_element(By.ID, "user-name")
username_box.send_keys("standard_user")

password_box = driver.find_element(By.ID, "password")
password_box.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Pause so the Products page can load
input("Check the Products page. Press Enter to continue...")

# -------------------------
# ADD TO CART
# -------------------------

add_to_cart = driver.find_element(
    By.CLASS_NAME, "btn_inventory"
)

add_to_cart.click()

print("Backpack added to cart")

# -------------------------
# OPEN CART
# -------------------------

input("Check that the cart shows 1. Press Enter to continue...")

cart_icon = driver.find_element(
    By.CLASS_NAME, "shopping_cart_link"
)

cart_icon.click()

print("Cart page opened")

# -------------------------
# CHECKOUT
# -------------------------

input("Check the Cart page. Press Enter to continue...")

checkout_button = driver.find_element(
    By.ID, "checkout"
)

checkout_button.click()

print("Checkout page opened")

# -------------------------
# VALIDATION TEST
# -------------------------

first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("Sahithi")

last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Reddy")

input("Leave postal code field empty. Press Enter to continue...")

continue_button = driver.find_element(
    By.ID, "continue"
)

continue_button.click()

print("Continue button clicked")

# Get the validation error
error_message = driver.find_element(
    By.CLASS_NAME, "error-message-container"
).text

print("Error message:", error_message)
assert "Postal Code is required" in error_message

print("Checkout validation test passed")


# Keep browser open
input("Check the error message. Press Enter to close...")

driver.quit()