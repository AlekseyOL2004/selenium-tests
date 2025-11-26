from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CartPage(BasePage):
    URL = "https://famo.ua/cart"
    ITEM_NAME = (By.CSS_SELECTOR, ".line-item")
    CLEAR_BUTTON = (By.NAME, "commit")

    def open(self):
        self.driver.get(self.URL)

    def has_items(self):
        try:
            self.find_element(self.ITEM_NAME)
            return True
        except:
            return False

    def clear(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.ITEM_NAME)
        )
        el = self.find_element(self.CLEAR_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
        self.driver.execute_script("arguments[0].click();", el)
