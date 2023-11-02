import pytest
import requests
import json
import time

def test_create_user():
    # задаем url, заполняем тело запроса
    url = "https://petstore.swagger.io/v2/user"
    request = {}
    request["id"] = 0
    request["username"] = "VasVas"
    request["firstName"] = "Vasiliy"
    request["lastName"] = "Vasilevich"
    request["email"] = "pochemybiinet@v.net"
    request["password"] = "qwerty"
    request["phone"] = "88005553535"
    request["userStatus"] = 1
    # отправляем запрос
    request_post = requests.post(url, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # проверяем что статус код ответа 500
    assert str(request_post).__contains__('200')

def test_create_user_negative():
    # задаем url, заполняем тело запроса
    url = "https://petstore.swagger.io/v2/user"
    request = {}
    request["id"] = 0
    request["username"] = "123"
    request["firstName"] = "Vasiliy"
    request["lastName"] = "Vasilevich"
    request["email"] = "pochemybiinet@v.net"
    request["password"] = "qwerty"
    request["phone"] = "88005553535"
    request["userStatus"] = 1254896448821
    # отправляем запрос
    request_post = requests.post(url, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # проверяем что статус код ответа 500, и параметр message
    assert str(request_post).__contains__('500')
    assert request_post.json()['message'] == "something bad happened"

def test_delete_user():
    # задаем url, заполняем тело запроса
    url = "https://petstore.swagger.io/v2/user/"
    request = {}
    request["id"] = 0
    request["username"] = "VasVas"
    request["firstName"] = "Vasiliy"
    request["lastName"] = "Vasilevich"
    request["email"] = "pochemybiinet@v.net"
    request["password"] = "qwerty"
    request["phone"] = "88005553535"
    request["userStatus"] = 1
    # отправляем запрос
    request_post = requests.post(url, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # задаем url и отправляем delete запрос
    url_del = url + request['username']
    # отправляем запрос на удаление
    request_del = requests.delete(url_del, verify=False)
    # проверяем ответ полученый на запрос
    print('view_request_delete = ', url_del, request_del)
    # проверяем что пользователь удален
    assert str(request_del).__contains__('200')

def test_delete_user_negative():
    # задаем url, заполняем тело запроса
    url = "https://petstore.swagger.io/v2/user/"
    request = {}
    request["id"] = 0
    request["username"] = "VasVas"
    request["firstName"] = "Vasiliy"
    request["lastName"] = "Vasilevich"
    request["email"] = "pochemybiinet@v.net"
    request["password"] = "qwerty"
    request["phone"] = "88005553535"
    request["userStatus"] = 1
    # отправляем запрос
    request_post = requests.post(url, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # задаем url, добавляем не существующего username и отправляем delete запрос
    url_del = "https://petstore.swagger.io/v2/user/" + str(request['email'])
    # отправляем запрос на удаление
    request_del = requests.delete(url_del, verify=False)
    # проверяем ответ полученый на запрос
    print('view_request_delete = ',json.dumps(request_del.json(), indent=4, sort_keys=True))
    # проверяем что пользователь удален
    assert str(request_del).__contains__('404')

def test_get_user():
    # задаем url, заполняем тело запроса
    url = "https://petstore.swagger.io/v2/user/"
    request = {}
    request["id"] = 0
    request["username"] = "VasVas"
    request["firstName"] = "Vasiliy"
    request["lastName"] = "Vasilevich"
    request["email"] = "pochemybiinet@v.net"
    request["password"] = "qwerty"
    request["phone"] = "88005553535"
    request["userStatus"] = 1
    # отправляем запрос
    request_post = requests.post(url, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # задаем url
    url_get = url + str(request['username'])
    # вызываем get запрос
    request_get = requests.get(url_get, verify=False)
    # получаем ответ
    print('view_result = ', json.dumps(request_get.json(), indent=4, sort_keys=True))
    # проверяем статус код
    assert str(request_get).__contains__('200')

def test_get_user_negative():
    # задаем url, заполняем тело запроса
    url = "https://petstore.swagger.io/v2/user/"
    request = {}
    request["id"] = 0
    request["username"] = "VasVas"
    request["firstName"] = "Vasiliy"
    request["lastName"] = "Vasilevich"
    request["email"] = "pochemybiinet@v.net"
    request["password"] = "qwerty"
    request["phone"] = "88005553535"
    request["userStatus"] = 1
    # отправляем запрос
    request_post = requests.post(url, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # задаем url c невалидным username, вызываем get запрос
    url = "https://petstore.swagger.io/v2/user/" + str(request['phone'])
    request_get = requests.get(url, verify=False)
    # получаем ответ
    print('view_result = ', json.dumps(request_get.json(), indent=4, sort_keys=True))
    # проверяем статус код и параметр message
    assert str(request_get).__contains__('404')
    assert request_get.json()['message'] == "User not found"

def test_put_user():
    # задаем url, заполняем тело запроса
    url = "https://petstore.swagger.io/v2/user/"
    request = {}
    request["id"] = 0
    request["username"] = "VasVas"
    request["firstName"] = "Vasiliy"
    request["lastName"] = "Vasilevich"
    request["email"] = "pochemybiinet@v.net"
    request["password"] = "qwerty"
    request["phone"] = "88005553535"
    request["userStatus"] = 1
    # отправляем запрос
    request_post = requests.post(url, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # задаем url
    url_put = url + str(request['username'])
    # заполняем тело запроса
    request_put = {}
    request_put["id"] = str(request_post.json()['message'])
    request_put["username"] = "VasVas2"
    request_put["firstName"] = "Vasiliy2"
    request_put["lastName"] = "Vasilevich2"
    request_put["email"] = "pochemybiinet@v.net2"
    request_put["password"] = "qwerty2"
    request_put["phone"] = "880055535352"
    request_put["userStatus"] = 1
    request_put_r = requests.put(url_put, json=request_put, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_put = ', json.dumps(request_put_r.json(), indent=4, sort_keys=True))
    # проверяем статус код
    assert str(request_put_r).__contains__('200')
    # формируем url
    url_get = url + str(request_put['username'])
    # вызываем get запрос
    request_get = requests.get(url_get, verify=False)
    # получаем ответ
    print('view_result = ', json.dumps(request_get.json(), indent=4, sort_keys=True))
    # проверяем статус код и поле username
    assert str(request_get).__contains__('200')
    assert request_get.json()['username'] == 'VasVas2'

def test_put_user_negative():
    # задаем url, заполняем тело запроса
    url = "https://petstore.swagger.io/v2/user/"
    request = {}
    request["id"] = 0
    request["username"] = "VasVas"
    request["firstName"] = "Vasiliy"
    request["lastName"] = "Vasilevich"
    request["email"] = "pochemybiinet@v.net"
    request["password"] = "qwerty"
    request["phone"] = "88005553535"
    request["userStatus"] = 1
    # отправляем запрос
    request_post = requests.post(url, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # задаем url
    url_put = url + str(request['username'])
    # заполняем тело запроса
    request_put = {}
    request_put["id"] = str(request_post.json()['message'])
    request_put["username"] = "VasVas2"
    request_put["firstName"] = "Vasiliy2"
    request_put["lastName"] = "Vasilevich2"
    request_put["email"] = "pochemybiinet@v.net2"
    request_put["password"] = "qwerty2"
    request_put["phone"] = "880055535352"
    request_put["userStatus"] = 1
    request_put_r = requests.put(url_put, json=request_put, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_put = ', json.dumps(request_put_r.json(), indent=4, sort_keys=True))
    # проверяем статус код
    assert str(request_put_r).__contains__('200')
    # задаем url с невалидным username
    url = "https://petstore.swagger.io/v2/user/" + str(request_put['phone'])
    # формируем пустое тело запроса
    request = {}
    #отправляем put запрос
    request_get = requests.get(url, json=request, verify=False)
    # Выводим содержимое ответа
    print('view = ', json.dumps(request_get.json(), indent=4, sort_keys=True))
    # проверяем что пользователь не найден
    assert str(request_get).__contains__('404')
    assert request_get.json()['message'] == 'User not found'