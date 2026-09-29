from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

username_box = driver.find_element(By.ID, "user-name")
username_box.send_keys("standard_user")

password_box = driver.find_element(By.ID, "password")
password_box.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

add_to_cart = driver.find_element(By.CLASS_NAME, "btn_inventory")
add_to_cart.click()

cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_icon.click()

remove_button = driver.find_element(By.ID, "remove-sauce-labs-backpack")

remove_button.click()

cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")

assert len(cart_items) == 0

print("Remove from cart test passed")

input("Press Enter to close the browser...")
driver.quit()