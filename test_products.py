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

# -------------------------
# PRODUCT NAME TEST
# -------------------------

product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

print("Product name:", product_name)

assert product_name != ""

print("Product name test passed")

# PRODUCT PRICE TEST

product_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

expected_price = "$29.99"

assert product_price == expected_price

print("Product price test passed")

# ADD TO CART TEST

add_to_cart = driver.find_element(By.CLASS_NAME, "btn_inventory")

add_to_cart.click()

cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

assert cart_count == "1"

print("Add to cart test passed")

# OPEN CART

cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")

cart_icon.click()

# CART ITEM TEST

cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

print("Cart item:", cart_item)

expected_item = "Sauce Labs Backpack"

assert cart_item == expected_item

print("Cart item test passed")

# Keep browser open
input("Press Enter to close the browser...")

# Close browser
driver.quit()