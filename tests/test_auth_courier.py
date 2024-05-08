import pytest
import allure
from edpoints.auth_courier import Auth

class TestAuthCourier:
    @allure.title("Проверка успешной авторизации курьера")
    @allure.description("Проверка 200 кода и полученное id - число")
    def test_auth_courier(self, auth_courier):
        response = auth_courier.auth_courier(self)
        assert response.status_code== 200 and type(response.json()["id"]) == int

    @allure.title("Проверка авторизации курьера с пустым логином")
    @allure.description("Проверка 400 кода и ответа 'Недостаточно данных для входа'")
    def test_auth_courier_with_empty_login(self, auth_courier):
        response = auth_courier.auth_courier_with_empty_login(self)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Проверка авторизации курьера с пустым паролем")
    @allure.description("Проверка 400 кода и ответа 'Недостаточно данных для входа'")
    def test_auth_courier_with_empty_pass(self, auth_courier):
        response = auth_courier.auth_courier_with_empty_pass(self)
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Проверка авторизации несуществующего курьера")
    @allure.description("Проверка 404 кода и ответа 'Учетная запись не найдена'")
    def test_auth_courier_with_fake_log_pass(self, auth_courier):
        response = auth_courier.auth_courier_with_fake_log_pass(self)
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"