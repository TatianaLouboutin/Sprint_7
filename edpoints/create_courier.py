import pytest
import requests
import urls
import random
import string
import allure

class CreateCourier:
    @allure.step('Генерируем данные')
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step('Создаем payload')
    def create_payload(self):
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return payload

    @allure.step('Создаем нового курьера с пустым логином или паролем, возвращаем POST запрос')
    def create_courier_with_empty_field(self, payload):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, data=payload)


    @allure.step('Создаем нового курьера, возвращаем POST запрос, удаляем курьера')
    def create_courier(self, payload):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, data=payload)



    @allure.step('Создаем нового курьера с пустым именем, возвращаем POST запрос')
    def create_courier_with_empty_first_name(self, payload_with_empty_firstname):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, data=payload_with_empty_firstname)



    @allure.step('Создаем одного и того же курьера второй раз, возвращаем POST запрос, удаляем курьера')
    def register_the_same_courier(self, payload):
        response = requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, data=payload)

        if response.status_code == 201:
            response = requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, data=payload)
        return response

    @allure.step('Удаляем курьера')
    def delete_courier(self, payload):
        response = requests.post(urls.BASE_URL + urls.COURIER_AUTH_ENDPOINT, data=payload)
        id_courier = response.json()['id']
        response = requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT + str(id_courier))


    @allure.step('Создаем нового курьера, возвращаем логин и пароль')
    def register_new_courier_and_return_login_password(self, payload_auth):
        response = requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, data=payload_auth)

        if response.status_code == 201:
            payload_auth.pop("firstName")
            return payload_auth






