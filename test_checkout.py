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

# Pause so we can see the Products page
input("Check the Products page. Press Enter to continue...")

# -------------------------
# ADD TO CART
# -------------------------

add_to_cart = driver.find_element(
    By.CLASS_NAME, "btn_inventory"
)

add_to_cart.click()

print("Backpack added to cart")

# Pause so we can see the cart
input("Check that the cart shows 1. Press Enter to continue...")

# -------------------------
# OPEN CART
# -------------------------

cart_icon = driver.find_element(
    By.CLASS_NAME, "shopping_cart_link"
)

cart_icon.click()

print("Cart page opened")

# Pause so we can see the Cart page
input("Check the Cart page. Press Enter to continue...")

# -------------------------
# CHECKOUT
# -------------------------

checkout_button = driver.find_element(
    By.ID, "checkout"
)

checkout_button.click()

print("Checkout page opened")

# Pause so we can see the Checkout Information page
input("Check the Checkout Information page. Press Enter to continue...")

# -------------------------
# CHECKOUT INFORMATION
# -------------------------

first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("Sahithi")

last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Reddy")

postal_code = driver.find_element(By.ID, "postal-code")
postal_code.send_keys("91302")

print("Checkout information entered")

continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

print("Checkout overview opened")

overview_item = driver.find_element(
    By.CLASS_NAME, "inventory_item_name"
).text

print("Overview item:", overview_item)

assert overview_item == "Sauce Labs Backpack"

print("Checkout overview item test passed")

item_price = driver.find_element(
    By.CLASS_NAME, "inventory_item_price"
).text

print("Item price:", item_price)

total_price = driver.find_element(
    By.CLASS_NAME, "summary_total_label"
).text

print("Order total:", total_price)

finish_button = driver.find_element(By.ID, "finish")
finish_button.click()

print("Finish button clicked")

confirmation = driver.find_element(
    By.CLASS_NAME, "complete-header"
).text

print("Confirmation:", confirmation)

assert confirmation == "Thank you for your order!"

print("Order completion test passed")

# Keep browser open
input("Check the confirmation page. Press Enter to close...")
driver.quit()