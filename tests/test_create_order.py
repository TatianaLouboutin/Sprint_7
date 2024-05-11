import data
import pytest
import allure
import urls
from edpoints.create_order import CreateOrder
import requests

class TestCreateOrder:
    @allure.title("Проверка успешного создания заказа самоката со всеми вариантами цвета")
    @allure.description("Проверка 201 кода, ответа 'track' == int")
    @pytest.mark.parametrize('order', data.TestDataCreateOrder.LST_ORDERS)
    def test_create_order(self, new_order, order):
        response = new_order.create_order(order)
        assert response.status_code == 201 and type(response.json()["track"]) == int
        id = response.json()["track"]
        payload = {"track": id }
        response = requests.put(urls.BASE_URL + urls.CANCEL_ORDER_ENDPOINT, data=payload)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("Проверка успешного возвращения списка заказов")
    @allure.description("Проверка возвращения списка, список не пустой")
    def test_get_orders_list(self, new_order):
        response = new_order.get_orders_list()
        assert response.json()['orders'] is not None
