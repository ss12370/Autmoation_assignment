import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.config import BASE_URL

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()

    # Disable notifications
    options.add_argument("--disable-notifications")
    options.add_experimental_option(
        "prefs",
        {"profile.default_content_setting_values.notifications": 2}
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()


# Screenshot on test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver", None)

        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            file_name = report.nodeid.replace("::", "_") + ".png"
            file_path = os.path.join(screenshot_dir, file_name)

            driver.save_screenshot(file_path)