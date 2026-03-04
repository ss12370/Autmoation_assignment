from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    FIRST_PRODUCT = (By.XPATH, "(//div[contains(@class,'product-card')])[1]")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.XPATH, "//span[contains(@class,'price')]")
    QUANTITY_INPUT = (By.XPATH, "//input[@type='number']")
    ADD_TO_CART = (By.XPATH, "//button[contains(text(),'Add to Cart')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def select_first_product(self):
        self.wait.until(
            EC.element_to_be_clickable(self.FIRST_PRODUCT)
        ).click()

    def get_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        ).text

    def is_price_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_PRICE)
        ).is_displayed()

    def is_quantity_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.QUANTITY_INPUT)
        ).is_displayed()

    def is_add_to_cart_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ADD_TO_CART)
        ).is_displayed()