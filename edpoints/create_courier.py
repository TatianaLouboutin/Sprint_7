import pytest
import requests
import urls
import random
import string
import allure

class CreateCourier:
    @allure.step('Создаем нового курьера, возвращаем POST запрос')
    def create_courier():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, data=payload)

    @allure.step('Создаем нового курьера с пустым логином, возвращаем POST запрос')
    def create_courier_with_empty_login():

        payload = {
            "login": "",
            "password": "assembler",
            "firstName": "Ivan"
        }

        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, data=payload)

    @allure.step('Создаем нового курьера с пустым паролем, возвращаем POST запрос')
    def create_courier_with_empty_pass():
        payload = {
            "login": "assembler",
            "password": "",
            "firstName": "Ivan"
        }

        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, data=payload)

    @allure.step('Создаем нового курьера с пустым именем, возвращаем POST запрос')
    def create_courier_with_empty_first_name():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": ""
        }

        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, data=payload)

    @allure.step('Создаем нового курьера с пустым именем, возвращаем логин и пароль')
    def register_new_courier_and_return_login_password():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login_pass = []

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass

    @allure.step('Создаем одного и того же курьера второй раз, возвращаем POST запрос')
    def register_the_same_courier():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login_pass = []

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)


        login_pass = {"login": login_pass[0], "password": login_pass[1]}
        response = requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, data=login_pass)
        return response

    @allure.step('Авторизуемся пользователем, возвращаем id курьера')
    def courier_return_id():
        courier = CreateCourier
        log_pass = courier.register_new_courier_and_return_login_password()
        payload = {"login": log_pass[0], "password": log_pass[1]}
        response = requests.post(urls.BASE_URL + urls.COURIER_AUTH_ENDPOINT, data=payload)
        id_courier = response.json()["id"]
        return id_courier


    @allure.step('Удаляем пользователя')
    def delete_courier(id):
        response = requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT + str(id))
        return response