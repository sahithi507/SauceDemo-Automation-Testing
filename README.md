# SauceDemo Automation Testing Project

## Project Overview

This project is a web application testing project developed using Python, Selenium WebDriver, and pytest.

The project automates common user workflows on the SauceDemo website and includes positive and negative test scenarios to validate application functionality and expected behavior.

## Technologies Used

- Python
- Selenium WebDriver
- pytest
- Google Chrome
- Visual Studio Code

## Test Scenarios

The automation suite covers the following scenarios:

1. Valid Login
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

These validation scenarios are included as separate test cases in the pytest suite.

## Project Structure

```text
SauceDemo-Automation-Testing/
│
├── tests/
│   ├── test_checkout_pytest.py
│   ├── test_checkout_validation_pytest.py
│   ├── test_invalid_login_pytest.py
│   ├── test_login_pytest.py
│   ├── test_logout_pytest.py
│   ├── test_products_pytest.py
│   └── test_remove_cart_pytest.py
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

The `tests/` directory contains the organized pytest automation suite. The Python files in the project root are the original standalone scripts.

## Installation and Setup

1. Clone or download the repository.
2. Open the project folder in Visual Studio Code.
3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Ensure Google Chrome is installed.
5. Run the automated test suite from the project root directory.

## Running the Tests

Execute the following command in the VS Code terminal:

```bash
python -m pytest -s
```

The pytest configuration is defined in `pytest.ini` to discover the organized test files.

## Test Results

The complete pytest test suite was executed successfully:

```text
9 passed
```

The nine test cases include the main login, product, cart, checkout, validation, and logout workflows.

## Skills Demonstrated

- Manual Testing
- Test Case Design
- Functional Testing
- Positive and Negative Testing
- UI Automation
- Selenium WebDriver
- Python Programming
- pytest
- Assertions and Explicit Waits
- Element Locators
- End-to-End Testing
- Checkout Validation
- Debugging and Test Failure Analysis

## Project Highlights

- Automated common SauceDemo user workflows using Selenium WebDriver.
- Implemented positive and negative test scenarios to validate application behavior.
- Used explicit waits to synchronize browser interactions and improve test execution reliability.
- Applied assertions to verify expected page behavior, messages, and validation results.
- Created reusable checkout validation logic for multiple required-field scenarios.
- Organized automated test cases into a dedicated `tests/` directory.
- Configured pytest test discovery through `pytest.ini`.
- Executed the test suite using pytest and recorded nine passing test cases.
- Documented project setup, dependencies, test scenarios, and execution instructions for reproducibility.
