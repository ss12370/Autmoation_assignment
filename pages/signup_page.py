from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class SignupPage(BasePage):
    PROFILE_ICON = (
        By.CSS_SELECTOR,
        "#__next div.header_and_megmenu header div.mobile_header div.header_options ul li.link_item.mbl_home_d_none.md_none > div"
    )

    MOBILE_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Mobile Number']")
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(text(),'Continue')]")
    
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    
    # Updated Email selector you provided
    EMAIL = (
        By.CSS_SELECTOR,
        "body > div.MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper > div > div > div.jsx-1717673607.login_form > form > div.jsx-1717673607.d-flex.align-items-center.position-relative.mt-2.w-100 > div > label > input"
    )
    
    DONE_BUTTON = (By.XPATH, "//button[contains(text(),'Create Account')]")

    def create_account(self, phone, otp, first_name, last_name, email):
        # Open profile/signup popup
        self.click(self.PROFILE_ICON)

        # Enter mobile number and continue
        self.type(self.MOBILE_INPUT, phone)
        self.click(self.CONTINUE_BUTTON)

        # Split OTP into digits
        otp_digits = list(otp)

        # OTP input selectors for each digit
        otp_selectors = [
            "body > div.MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper > div > div > div.jsx-1027105241.position-relative > form > div.jsx-1027105241.otp_content > div.jsx-1027105241.row.justify-content-center > div.jsx-1027105241.col-12.mobile_otp_new.position-relative.d-flex.justify-content-center > div > div:nth-child(1) > input",
            "body > div.MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper > div > div > div.jsx-1027105241.position-relative > form > div.jsx-1027105241.otp_content > div.jsx-1027105241.row.justify-content-center > div.jsx-1027105241.col-12.mobile_otp_new.position-relative.d-flex.justify-content-center > div > div:nth-child(2) > input",
            "body > div.MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper > div > div > div.jsx-1027105241.position-relative > form > div.jsx-1027105241.otp_content > div.jsx-1027105241.row.justify-content-center > div.jsx-1027105241.col-12.mobile_otp_new.position-relative.d-flex.justify-content-center > div > div:nth-child(3) > input",
            "body > div.MuiDialog-root > div.MuiDialog-container.MuiDialog-scrollPaper > div > div > div.jsx-1027105241.position-relative > form > div.jsx-1027105241.otp_content > div.jsx-1027105241.row.justify-content-center > div.jsx-1027105241.col-12.mobile_otp_new.position-relative.d-flex.justify-content-center > div > div:nth-child(4) > input",
        ]

        # Enter OTP digit by digit
        for selector, digit in zip(otp_selectors, otp_digits):
            otp_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
            otp_input.clear()
            otp_input.send_keys(digit)

        # Wait for OTP auto-verification
        time.sleep(3)

        # Enter first name and last name
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)

        # Wait explicitly for email input to appear after last name
        email_input = self.wait.until(EC.element_to_be_clickable(self.EMAIL))
        email_input.clear()
        email_input.send_keys(email)

        # Click "Create Account" button
        self.click(self.DONE_BUTTON)
        print("User account created successfully")

