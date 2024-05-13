import urls
from edpoints.create_courier import CreateCourier
import requests
import allure
class Auth(CreateCourier):
    @allure.step('Авторизуемся созданным пользователем, возвращаем POST запрос')
    def auth_courier(self, payload_auth):
        payload = self.register_new_courier_and_return_login_password(payload_auth)
        response = requests.post(urls.BASE_URL + urls.COURIER_AUTH_ENDPOINT, data=payload)
        return response

    @allure.step('Авторизуемся любым payload, возвращаем POST запрос')
    def auth_courier_with_any_payload(self, payload):
        response = requests.post(urls.BASE_URL + urls.COURIER_AUTH_ENDPOINT, data=payload)
        return response



