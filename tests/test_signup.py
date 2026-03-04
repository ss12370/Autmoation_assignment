import pytest
from utils.driver_factory import get_driver
from selenium.webdriver.common.by import By 
from pages.signup_page import SignupPage
from data.test_data import *


@pytest.fixture
def driver():
    driver = get_driver()
    driver.get("https://dev.trulyfree.com/")
    yield driver
    driver.quit()


def test_user_can_signup(driver):

    signup = SignupPage(driver)

    signup.create_account(
        phone=PHONE,
        otp=OTP,
        first_name=FIRST_NAME,
        last_name=LAST_NAME,
        email=EMAIL
    )

    # Simple validation
    assert driver.find_element(By.XPATH, "//span[contains(text(),'Brands')]").is_displayed()