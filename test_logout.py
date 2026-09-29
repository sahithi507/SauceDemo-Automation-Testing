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

# Pause so we can see Products page
input("Check the Products page. Press Enter to continue...")

# -------------------------
# OPEN MENU
# -------------------------

menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
menu_button.click()

# Pause so we can see the menu
input("Check that the menu opened. Press Enter to continue...")

# -------------------------
# LOGOUT
# -------------------------

logout_button = driver.find_element(By.ID, "logout_sidebar_link")

print("Logout button found")

logout_button.click()

print("Logout button clicked")

# -------------------------
# VERIFY LOGIN PAGE
# -------------------------

username_box = driver.find_element(By.ID, "user-name")

assert username_box.is_displayed()

print("Logout test passed")

# Keep browser open
input("Check the Login page. Press Enter to close...")

driver.quit()