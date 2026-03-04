import pytest
from utils.driver_factory import get_driver
from selenium.webdriver.common.by import By 
from pages.signup_page import SignupPage



@pytest.fixture
def driver():
    driver = get_driver()
    driver.get("https://dev.trulyfree.com/")
    yield driver
    driver.quit()


def test_user_can_signup(driver):

    signup = SignupPage(driver)

    signup.create_account(
        phone="9148358383",
        otp="1111",
        first_name="QA",
        last_name="Tester",
        email="qatester123@gmail.com"
    )

    # Simple validation
    assert driver.find_element(By.XPATH, "//span[contains(text(),'Brands')]").is_displayed()