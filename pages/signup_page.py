from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignupPage(BasePage):
    URL = "https://famo.ua/signup"
    EMAIL = (By.NAME, "spree_user[email]")
    PASSWORD = (By.NAME, "spree_user[password]")
    PASSWORD2 = (By.NAME, "spree_user[password_confirmation]")
    PHONE = (By.NAME,"spree_user[phone_number]")
    SUBMIT = (By.NAME, "commit")
    ERRORS = (By.CSS_SELECTOR, ".errorExplanation>ul>li")

    def open(self):
        self.driver.get(self.URL)

    def input(self, email="", password="", password2="", phone=""):
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.type(self.PASSWORD2, password2)
        self.type(self.PHONE, phone)
        self.click(self.SUBMIT)

    def get_error_messages(self):
        errors = self.driver.find_elements(*self.ERRORS)
        return [e.text.strip() for e in errors if e.text.strip()]
