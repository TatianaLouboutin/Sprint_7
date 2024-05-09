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
    new_courier = CreateCourier()
    return new_courier


@allure.step("Авторизация курьера")
@pytest.fixture(scope='function')
def auth_courier():
    courier = Auth()
    return courier


@allure.step("Создание заказа")
@pytest.fixture(scope='function')
def new_order():
    new_order = CreateOrder()
    return new_order


