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



    @allure.step('Запрашиваем список заказов, возвращаем GET запрос')
    def get_orders_list(self):
        response = requests.get(urls.BASE_URL + urls.LIST_ORDERS_ENDPOINT)
        return response