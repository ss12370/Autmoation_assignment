from pages.brands_page import BrandsPage


def test_navigate_to_campus_brand(driver):
    brand = BrandsPage(driver)

    brand.click_brands()
    brand.search_brand("Campus")
    brand.select_campus_brand()

    assert "campus" in driver.current_url.lower()