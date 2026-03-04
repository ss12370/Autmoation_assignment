from pages.brands_page import BrandsPage
from pages.product_page import ProductPage


def test_plp_to_pdp_navigation(driver):

    # ---- Navigate to Campus Brand ----
    brand = BrandsPage(driver)
    brand.click_brands()
    brand.search_brand("Campus")
    brand.select_campus_brand()

    # ---- Select Product ----
    product = ProductPage(driver)
    product.select_first_product()

    # ---- Validations ----
    product_name = product.get_product_name()

    assert product_name != ""
    assert product.is_price_displayed()
    assert product.is_quantity_visible()
    assert product.is_add_to_cart_visible()