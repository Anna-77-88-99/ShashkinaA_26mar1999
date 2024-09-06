import allure
import requests

class DataAPI:
    def __init__(self, baseurl: str):
        self._baseurl = baseurl

    @allure.step("с помощью id товара: {id_prod} добавить {type_ops} товар в корзину")
    def add_prod_by_id(self, id_prod: int, type_ops: str):
        path = ("{url_value}/ajax/basketOrder.php".format(url_value = self._baseurl))
        json_data = {
            "idCookie":"244995",
            "idProd":id_prod,
            "type":type_ops
            }
        resp = requests.post(path, json=json_data)
        return resp.status_code
    
    @allure.step("с помощью id товара: {id_prod} изменить количество товара {type_ops} в корзине")
    def increase_prod_by_id(self, id_prod: int, type_ops: str):
        path = ("{url_value}/ajax/basketOrder.php".format(url_value = self._baseurl))
        json_data = {
            "idCookie":"244995",
            "idProd":id_prod,
            "type":type_ops
            }
        resp = requests.post(path, json=json_data)
        return resp.status_code
    
    @allure.step("с помощью id товара: {id_prod} удалить {type_ops} товар из корзины")
    def delete_prod_by_id(self, id_prod: int, type_ops: str):
        path = ("{url_value}/ajax/basketOrder.php".format(url_value = self._baseurl))
        json_data = {
            "idCookie":"244995",
            "idProd":id_prod,
            "type":type_ops
            }
        resp = requests.post(path, json=json_data)
        return resp.status_code