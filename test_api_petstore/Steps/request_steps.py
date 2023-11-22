import json

import requests
import allure

# Отправка запроса и получение ответа для метода POST
# url - эндпоинт
# request - JSON
def request_post(url, request):
    with allure.step("Отправка запросов и получение ответа для метода POST"):
        request = requests.post(url, json=request, verify=False)
        # выводим ответ на запрос в формате json
        print('result_post=', json.dumps(request.json(), indent=4, sort_keys=True))
        return request

# Отправка запроса и получение ответа для метода GET
# url - эндпоинт
def request_get(url):
    with allure.step("Отправка запросов и получение ответа для метода GET"):
        request = requests.get(url, verify=False)
        print('result_get=', json.dumps(request.json(), indent=4, sort_keys=True))
        return request


# Отправка запроса и получение ответа для метода  PUT
# url - эндпоинт
def request_put(url, request):
    with allure.step("Отправка запросов и получение ответа для метода PUT"):
        request = requests.put(url, json=request, verify=False)
        print('result_put=', json.dumps(request.json(), indent=4, sort_keys=True))
        return request

# Отправка запроса и получение ответа для метода DELETE
# url - эндпоинт
def request_delete(url):
    with allure.step("Отправка запросов и получение ответа для метода DELETE"):
        request = requests.delete(url, verify=False)
        print('result_delete=', request)
        return request


# Отправка запроса и получение ответа для метода POST c upload
# url - эндпоинт
def request_file(url, file):
    with allure.step("Отправка запроса и получение ответа для метода POST c upload"):
        request = requests.post(url, files=file, verify=False)
        print('result_upload_file=', request.json())
        return request


# Отправка запроса и получение ответа для метода POST c data
# url - эндпоинт
def request_data(url, data):
    with allure.step("Отправка запроса и получение ответа для метода POST c data"):
        request = requests.post(url, data=data, verify=False)
        print('result_upload_data=', request.json(), data)
        return request

