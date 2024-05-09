import data
import pytest
import allure
import requests
import urls



class CreateOrder:

    @allure.step('Создаем новый заказ, возвращаем POST запрос, отменяем запрос')
    def create_order(self, order):
        response = requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, data=order)
        return response
        id = response.json()["track"]
        payload = {"track": id}
        response = requests.put(urls.BASE_URL + urls.CANCEL_ORDER_ENDPOINT, data=payload)



    @allure.step('Запрашиваем список заказов, возвращаем GET запрос')
    def get_orders_list(self):
        response = requests.get(urls.BASE_URL + urls.LIST_ORDERS_ENDPOINT)
        return response