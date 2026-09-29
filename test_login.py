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

products_title = driver.find_element(By.CLASS_NAME, "title").text

assert products_title == "Products"

print("Login test passed")

product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

print("Product name:", product_name)

assert product_name != ""

print("Product name test passed")

input("Press Enter to close the browser...")
driver.quit()