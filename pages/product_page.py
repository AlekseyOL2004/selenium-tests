from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add-to-cart-button")

    def open(self, product_url):
        self.driver.get(product_url)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
