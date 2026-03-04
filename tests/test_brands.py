from pages.brands_page import BrandsPage
from utils.logger import get_logger
from pages.brands_page import BrandsPage


def test_navigate_to_campus_brand(driver):
    brand = BrandsPage(driver)

    brand.click_brands()
    brand.search_brand("Campus")
    brand.select_campus_brand()

    assert "campus" in driver.current_url.lower()


logger = get_logger()


def test_navigate_to_campus_brand(driver):

    logger.info("Starting brand navigation test")

    brand = BrandsPage(driver)

    logger.info("Clicking brands menu")
    brand.click_brands()

    logger.info("Searching Campus brand")
    brand.search_brand("Campus")

    logger.info("Brand navigation completed")

