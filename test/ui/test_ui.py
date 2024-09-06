import allure
from pages.DataUI import DataUi

@allure.id("TESTUI-1")
@allure.epic("ДИКИЙ СБОР UI")
@allure.title("Добавить товар")
@allure.description("Добавление товара в корзину")
@allure.feature("READ")
@allure.severity("blocker")
def test_order_product(browser):
    web_page = DataUi(browser)
    web_page.go()
    web_page.order_product()
    web_page.open_basket()
    price = web_page.get_price()
    with allure.step("Проверить, что цена товара в корзине корректная"):
        assert price == "1400"

@allure.id("TESTUI-2")
@allure.epic("ДИКИЙ СБОР UI")
@allure.title("Изменить количество товара")
@allure.description("Изменение количества товара в корзине")
@allure.feature("READ")
@allure.severity("blocker")
def test_increase_product(browser):
    web_page = DataUi(browser)
    web_page.go()
    web_page.order_product()
    web_page.open_basket()
    price = web_page.increase_value()
    with allure.step("Проверить, что цена товара в корзине корректная"):
        assert price == "2800"

@allure.id("TESTUI-3")
@allure.epic("ДИКИЙ СБОР UI")
@allure.title("Удалить товар из корзины")
@allure.description("Удаление товара из корзины")
@allure.feature("READ")
@allure.severity("blocker")
def test_remove_product(browser):
    web_page = DataUi(browser)
    web_page.go()
    web_page.order_product()
    web_page.open_basket()
    text_value = web_page.delete_product()
    with allure.step("Проверить, что корзина пуста"):
        assert text_value == "Корзина пуста, необходимо это исправить"