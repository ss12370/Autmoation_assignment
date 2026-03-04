from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BrandsPage:

    BRANDS_MENU = (By.XPATH, "//span[contains(text(),'Brands')]")
    SEARCH_BOX = (By.CSS_SELECTOR, "input[placeholder='Search Brands']")
    CAMPUS_OPTION = (By.XPATH, "//a[contains(.,'Campus')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    def click_brands(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BRANDS_MENU)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )

    def search_brand(self, brand_name):
        search = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BOX)
        )
        search.clear()
        search.send_keys(brand_name)
        search.send_keys(Keys.ENTER)

        # 🔥 Wait for search results to update
        self.wait.until(
            EC.presence_of_element_located(self.CAMPUS_OPTION)
        )

    def select_campus_brand(self):
        campus = self.wait.until(
            EC.element_to_be_clickable(self.CAMPUS_OPTION)
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", campus)
        campus.click()