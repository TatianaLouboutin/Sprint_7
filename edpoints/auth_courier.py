import urls
from edpoints.create_courier import CreateCourier
import requests
import allure
class Auth(CreateCourier):
    @allure.step('Авторизуемся созданным пользователем, возвращаем POST запрос')
    def auth_courier(self):
        courier = Auth
        log_pass = courier.register_new_courier_and_return_login_password()
        payload = {"login": log_pass[0], "password": log_pass[1]}
        response = requests.post(urls.BASE_URL + urls.COURIER_AUTH_ENDPOINT, data=payload)
        return response

    @allure.step('Авторизуемся пустым логином, возвращаем POST запрос')
    def auth_courier_with_empty_login(self):
        payload = {"login": "", "password": "qwe1223"}
        response = requests.post(urls.BASE_URL + urls.COURIER_AUTH_ENDPOINT, data=payload)
        return response

    @allure.step('Авторизуемся пустым паролем, возвращаем POST запрос')
    def auth_courier_with_empty_pass(self):
        payload = {"login": "Ivan", "password": ""}
        response = requests.post(urls.BASE_URL + urls.COURIER_AUTH_ENDPOINT, data=payload)
        return response

    @allure.step('Авторизуемся несуществующим пользователем, возвращаем POST запрос')
    def auth_courier_with_fake_log_pass(self):
        payload = {"login": "Ivan", "password": "1111111111"}
        response = requests.post(urls.BASE_URL + urls.COURIER_AUTH_ENDPOINT, data=payload)
        return response

