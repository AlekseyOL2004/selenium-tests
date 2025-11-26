# pages/home_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://famo.ua/"
    SEARCH_INPUT = (By.NAME, "search[with_name_or_sku]")

    def open(self):
        self.driver.get(self.URL)

    def search(self, text):
        search_field = self.find_element(self.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(text)
        search_field.send_keys(Keys.RETURN)
