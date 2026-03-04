# QA Automation Framework

This project is an end-to-end test automation framework built using **Python, Selenium, and PyTest** following the **Page Object Model (POM)** design pattern.  
The goal of this framework is to automate common user flows, validate application behavior through assertions, and produce clear execution reports for test runs.

The framework is structured in a modular way so that new tests, pages, and utilities can be added easily without affecting existing code.

---

## Tech Stack

- **Python**
- **Selenium WebDriver**
- **PyTest**
- **PyTest HTML Reporting**
- **Page Object Model (POM)**

---

## Project Structure


TFM
│
├── config
│ └── config.py # Environment configuration
│
├── data
│ └── test_data.py # Test data used across tests
│
├── pages # Page Object classes
│ ├── brands_page.py
│ ├── product_page.py
│ └── signup_page.py
│
├── tests # Test cases
│ ├── test_brands.py
│ ├── test_product.py
│ └── test_signup.py
│
├── utils # Utility modules
│ ├── driver_factory.py
│ └── logger.py
│
├── logs # Execution logs
├── reports # HTML test reports
├── screenshots # Screenshots captured on test failure
│
├── conftest.py # PyTest fixtures and driver setup
├── pytest.ini # PyTest configuration
├── run_tests.py # Script to run tests with timestamped reports
├── requirements.txt
└── README.md


---

## Setup Instructions

### 1. Clone the repository


git clone https://github.com/ss12370/Autmoation_assignment.git

cd Autmoation_assignment


### 2. Create a virtual environment


python -m venv venv


Activate it:


venv\Scripts\activate


### 3. Install project dependencies


pip install -r requirements.txt


---

## Running the Tests

To run all tests:


python -m pytest


To run tests with an HTML report:


python -m pytest tests --html=reports/report.html --self-contained-html


After execution, open the report:


reports/report.html


---

## Running Tests with Timestamped Reports

You can also execute tests using the provided runner script:


python run_tests.py


Each execution creates a new report file with a timestamp, making it easier to track test history.

Example:


reports/
report_2026-03-05_11-40-12.html
report_2026-03-05_11-45-28.html


---

## Framework Design

### Page Object Model (POM)

Each page of the application is represented as a separate class inside the `pages` directory.  
Locators and UI interactions are defined in these classes, while test logic remains inside the `tests` folder. This keeps the test code clean and maintainable.

### PyTest Fixtures

WebDriver initialization and teardown are handled using PyTest fixtures in `conftest.py`.  
This allows tests to reuse the same setup without repeating code.

### Configuration Management

Application settings such as base URL and timeouts are stored in `config/config.py`.  
This makes it easy to switch environments without modifying test files.

### Logging

Execution logs are stored in the `logs` directory.  
Logs help track test steps and simplify debugging when failures occur.

### Screenshots on Failure

If a test fails, the framework automatically captures a screenshot and saves it in the `screenshots` folder.

---

## Features

- End-to-end user flow automation
- Clean Page Object Model implementation
- PyTest based test execution
- HTML execution reports
- Automatic screenshot capture on failures
- Logging support for debugging
- Centralized configuration management
- Separate test data management
- Modular and scalable framework design

---

## Author

**Suraj G**