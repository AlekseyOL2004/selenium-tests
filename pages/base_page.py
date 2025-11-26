# pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """Відкрити сторінку"""
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        """Пошук одного елемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator, timeout=10):
        """Клік по елементу"""
        element = self.find_element(locator, timeout)
        element.click()

    def type(self, locator, text, timeout=10):
        """Ввести текст у поле"""
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator, timeout=10):
        """Перевірити видимість елемента"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False
