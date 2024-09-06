import allure
from pages.DataAPI import DataAPI

@allure.id("TESTAPI-1")
@allure.epic("ДИКИЙ СБОР API")
@allure.title("Добавить товар по id")
@allure.description("Добавление товара в корзину по id товара")
@allure.feature("READ")
@allure.severity("blocker")
def test_add_product(api_client: DataAPI, test_data: dict):
    result_api = api_client.add_prod_by_id(test_data.get("id_prod_value"), test_data.get("type_add_value"))
    with allure.step("Проверить статус код 200"):
        assert result_api == 200

@allure.id("TESTAPI-2")
@allure.epic("ДИКИЙ СБОР API")
@allure.title("Изменить количество товара по id")
@allure.description("Изменение количества товара в корзине по id товара")
@allure.feature("READ")
@allure.severity("blocker")
def test_plus_product(api_client: DataAPI, test_data: dict):
    result_api = api_client.increase_prod_by_id(test_data.get("id_prod_value"), test_data.get("type_plus_value"))
    with allure.step("Проверить статус код 200"):
        assert result_api == 200

@allure.id("TESTAPI-3")
@allure.epic("ДИКИЙ СБОР API")
@allure.title("Удалить товар из корзины по id")
@allure.description("Удаление товара из корзины по id товара")
@allure.feature("READ")
@allure.severity("blocker")
def test_delete_product(api_client: DataAPI, test_data: dict):
    result_api = api_client.delete_prod_by_id(test_data.get("id_prod_value"), test_data.get("type_delete_value"))
    with allure.step("Проверить статус код 200"):
        assert result_api == 200