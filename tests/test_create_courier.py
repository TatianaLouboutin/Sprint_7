import pytest
import allure
from edpoints.create_courier import CreateCourier
import data

class TestCreateCourier:
    @allure.title("Проверка успешной регистрации курьера")
    @allure.description("Проверка 201 кода и ответа 'ok' == True")
    def test_text_and_code(self, new_courier):
        response = new_courier.create_courier()
        assert response.status_code == 201 and response.json()["ok"] == True


    @allure.title("Проверка регистрации курьера с пустым логином")
    @allure.description("Проверка 400 кода и ответа 'Недостаточно данных для создания учетной записи'")
    def test_create_courier_with_empty_login(self, new_courier):
        payload = { "login": "", "password": "assembler", "firstName": "Ivan"}
        response = new_courier.create_courier_with_empty_field(payload)
        assert response.status_code == 400 and response.json()["message"] == data.TestDataCreateOrder.ANSWER_400

    @allure.title("Проверка регистрации курьера с пустым паролем")
    @allure.description("Проверка 400 кода и ответа 'Недостаточно данных для создания учетной записи'")
    def test_create_courier_with_empty_pass(self, new_courier):
        payload = {"login": "assembler", "password": "", "firstName": "Ivan"}
        response = new_courier.create_courier_with_empty_field(payload)
        assert response.status_code == 400 and response.json()["message"] == data.TestDataCreateOrder.ANSWER_400

    @allure.title("Проверка регистрации курьера с пустым именем")
    @allure.description("Проверка 201 кода и ответа 'ok' == True")
    def test_create_courier_with_empty_first_name(self, new_courier):
        response = new_courier.create_courier_with_empty_first_name()
        assert response.status_code == 201 and response.json()["ok"] == True

    @allure.title("Проверка невозможности регистрации одного и того же курьера второй раз")
    @allure.description("Проверка 409 кода и ответа 'Этот логин уже используется. Попробуйте другой.'")
    def test_register_the_same_courier(self, new_courier):
        response = new_courier.register_the_same_courier()
        assert response.status_code == 409 and response.json()["message"] == data.TestDataCreateOrder.ANSWER_409




