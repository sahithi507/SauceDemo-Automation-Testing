# SauceDemo Automation Testing Project

## Project Overview

This project is a web application testing project created using Python, Selenium WebDriver, and pytest.

The project automates common user workflows on the SauceDemo website and includes both positive and negative test scenarios.

## Technologies Used

- Python
- Selenium WebDriver
- pytest
- Google Chrome
- VS Code

## Test Scenarios

The automation suite covers:

1. Login
2. Invalid Login
3. Product Verification
4. Add Product to Cart
5. Remove Product from Cart
6. Checkout
7. Checkout Field Validation
8. Logout

## Checkout Validation Tests

The checkout validation tests verify required-field behavior for:

- Empty checkout fields
- Missing Last Name
- Missing Postal Code

## Project Structure

```text
SauceDemo_Automation/
│
├── tests/
│   ├── test_login_pytest.py
│   ├── test_invalid_login_pytest.py
│   ├── test_products_pytest.py
│   ├── test_remove_cart_pytest.py
│   ├── test_checkout_pytest.py
│   ├── test_checkout_validation_pytest.py
│   └── test_logout_pytest.py
│
├── test_login.py
├── test_invalid_login.py
├── test_products.py
├── test_remove_cart.py
├── test_checkout.py
├── test_checkout_validation.py
├── test_logout.py
│
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Running the Tests

Open the VS Code terminal in the project folder and run:

```powershell
python -m pytest -s
```

## Test Result

The complete pytest test suite passed successfully:

```text
9 passed
```

## Skills Demonstrated

- Manual Testing
- Test Case Design
- Functional Testing
- Positive and Negative Testing
- UI Automation
- Selenium WebDriver
- Python
- pytest
- Assertions
- Explicit Waits
- Element Locators
- End-to-End Testing
- Checkout Validation
- Debugging and Test Failure Analysis

## Project Highlights

- Automated complete user workflows using Selenium WebDriver.
- Used explicit waits to synchronize automation with the web application.
- Added assertions to verify expected application behavior.
- Tested both successful and unsuccessful user scenarios.
- Created reusable checkout validation logic.
- Organized pytest test cases into a dedicated `tests` folder.
- Executed the complete test suite using pytest, with all 9 tests passing.