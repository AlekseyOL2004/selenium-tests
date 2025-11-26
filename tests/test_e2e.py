import time
import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.account_page import AccountPage

BASE_PRODUCT = "https://famo.ua/products/svitshot-z-vyshyvkoiu-na-flisi-sw-f-532-102043"

@pytest.mark.skip(reason="Тимчасово вимкнено через зміну об'єкту")
def test_login_and_add_to_cart(driver):
    # 1️⃣ Логін
    login = LoginPage(driver)
    login.open()
    login.login("knm251_oos@student.ztu.edu.ua", "VdAHw4KxQGVyx!S")
    account = AccountPage(driver)
    assert account.is_logged_in(), "Логін не успішний"

    # 2️⃣ Відкрити сторінку товару і додати в кошик
    product = ProductPage(driver)
    product.open(BASE_PRODUCT)
    product.add_to_cart()

    # 3️⃣ Перевірка кошика
    cart = CartPage(driver)
    cart.open()
    time.sleep(2)
    y = cart.has_items()
    cart.clear()
    assert y, "Кошик повинен містити хоча б 1 товар"

