from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://famo.ua/login"
    EMAIL = (By.NAME, "spree_user[login]")
    PASSWORD = (By.NAME, "spree_user[password]")
    SUBMIT = (By.NAME, "commit")
    ERROR_ALERT = (By.CSS_SELECTOR, ".error, .alert-danger, .validation-message")

    def open(self):
        self.driver.get(self.URL)

    def login(self, email, password):
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def has_error(self):
        return self.is_visible(self.ERROR_ALERT)
