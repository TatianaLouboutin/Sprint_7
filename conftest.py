import pytest
import requests
import urls
import allure
from edpoints.create_courier import CreateCourier
from edpoints.auth_courier import Auth
from edpoints.create_order import CreateOrder


@allure.step("Создание объекта CreateCourier")
@pytest.fixture(scope='function')
def new_courier():
    new_courier = CreateCourier()
    return new_courier


@allure.step("Создание объекта Auth")
@pytest.fixture(scope='function')
def auth_courier():
    courier = Auth()
    return courier


@allure.step("Создание объекта CreateOrder")
@pytest.fixture(scope='function')
def new_order():
    new_order = CreateOrder()
    yield new_order


@allure.step("Создание payload и удаление курьера по окончании теста")
@pytest.fixture(scope='function')
def payload_auth():
    new_courier = CreateCourier()
    payload = new_courier.create_payload()
    yield payload
    new_courier.delete_courier(payload)

@allure.step("Создание payload и удаление курьера по окончании теста")
@pytest.fixture(scope='function')
def payload():
    new_courier = CreateCourier()
    payload = new_courier.create_payload()
    yield payload
    payload.pop("firstName")
    new_courier.delete_courier(payload)

@allure.step("Создание payload с пустым firstName и удаление курьера по окончании теста")
@pytest.fixture(scope='function')
def payload_with_empty_firstname():
    new_courier = CreateCourier()
    payload = new_courier.create_payload()
    payload["firstName"] = ""
    yield payload
    payload.pop("firstName")
    new_courier.delete_courier(payload)





