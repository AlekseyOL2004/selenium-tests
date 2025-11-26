from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AccountPage(BasePage):
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".logout_button")

    def is_logged_in(self, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.LOGOUT_BUTTON)
            )
            return True
        except:
            return False
