import pytest
import requests
import urls
import allure
from edpoints.create_courier import CreateCourier
from edpoints.auth_courier import Auth
from edpoints.create_order import CreateOrder


@allure.step("Создание курьера")
@pytest.fixture(scope='function')
def new_courier():
    new_courier = CreateCourier
    yield new_courier
    id = new_courier.courier_return_id
    new_courier.delete_courier(id)


@allure.step("Авторизация курьера и удаление его по завершении")
@pytest.fixture(scope='function')
def auth_courier():
    courier = Auth
    yield courier
    id = courier.courier_return_id
    courier.delete_courier(id)


@allure.step("Создание заказа")
@pytest.fixture(scope='function')
def new_order():
    new_order = CreateOrder
    return new_order

