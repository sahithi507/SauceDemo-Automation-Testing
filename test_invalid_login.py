from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username_box = driver.find_element(By.ID, "user-name")
username_box.send_keys("standard_user")

password_box = driver.find_element(By.ID, "password")
password_box.send_keys("wrong_password")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text

expected_error = "Epic sadface: Username and password do not match any user in this service"

assert error_message == expected_error

print("Invalid login test passed")


input("Press Enter to close the browser...")
driver.quit()