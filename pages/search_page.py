# pages/search_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class SearchPage(BasePage):
    URL = "https://famo.ua/t/tovary"
    SEARCH_INPUT = (By.NAME, "search[with_name_or_sku]")
    PRODUCT_LIST = (By.CSS_SELECTOR, ".product-listing-item")
    NO_RESULTS = (By.CSS_SELECTOR, "[data-hook='products_search_results_heading_no_results_found']")

    def open(self):
        self.driver.get(self.URL)

    def is_result_search(self):
        wait = WebDriverWait(self.driver, 3)
        try:
            wait.until(lambda d: 
                d.find_elements(*self.PRODUCT_LIST) or 
                d.find_elements(*self.NO_RESULTS)
            )
            if self.driver.find_elements(*self.PRODUCT_LIST):
                return True
            elif self.driver.find_elements(*self.NO_RESULTS):
                return False
            else:
                return None
        except:
            return None
