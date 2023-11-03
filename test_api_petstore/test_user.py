import pytest
import requests
import json
from resources import urls as urls
from Steps import support_steps as support_steps

@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_create_user():
    # заполняем тело запроса
    request = {}
    request["id"] = 0
    request["username"] = support_steps.generate_random_letter_string(5)
    request["firstName"] = support_steps.generate_random_letter_string(6)
    request["lastName"] = support_steps.generate_random_letter_string(7)
    request["email"] = support_steps.generate_random_letter_string_mail(8)
    request["password"] = support_steps.generate_random_letter_string(5)
    request["phone"] = support_steps.generate_random_number_string(11)
    request["userStatus"] = support_steps.generate_random_number_string(5)
    # отправляем запрос
    request_post = requests.post(urls.url_user, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # проверяем что статус код ответа 500
    assert str(request_post).__contains__('200')

@pytest.mark.full_regression
def test_create_user_negative():
    # заполняем тело запроса
    request = {}
    request["id"] = 0
    request["username"] = support_steps.generate_random_letter_string(5)
    request["firstName"] = support_steps.generate_random_letter_string(6)
    request["lastName"] = support_steps.generate_random_letter_string(7)
    request["email"] = support_steps.generate_random_letter_string_mail(8)
    request["password"] = support_steps.generate_random_letter_string(5)
    request["phone"] = support_steps.generate_random_number_string(11)
    request["userStatus"] = support_steps.generate_random_number_string(13)
    # отправляем запрос
    request_post = requests.post(urls.url_user, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # проверяем что статус код ответа 500, и параметр message
    assert str(request_post).__contains__('500')
    assert request_post.json()['message'] == "something bad happened"

@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_delete_user():
    # заполняем тело запроса
    request = {}
    request["id"] = 0
    request["username"] = support_steps.generate_random_letter_string(5)
    request["firstName"] = support_steps.generate_random_letter_string(6)
    request["lastName"] = support_steps.generate_random_letter_string(7)
    request["email"] = support_steps.generate_random_letter_string_mail(8)
    request["password"] = support_steps.generate_random_letter_string(5)
    request["phone"] = support_steps.generate_random_number_string(11)
    request["userStatus"] = support_steps.generate_random_number_string(5)
    # отправляем запрос
    request_post = requests.post(urls.url_user, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # задаем url и отправляем delete запрос
    # отправляем запрос на удаление
    request_del = requests.delete(urls.url_user_get(request['username']), verify=False)
    # проверяем ответ полученый на запрос
    print('view_request_delete = ', urls.url_user_get(request['username']), request_del)
    # проверяем что пользователь удален
    assert str(request_del).__contains__('200')

@pytest.mark.full_regression
def test_delete_user_negative():
    # заполняем тело запроса
    request = {}
    request["id"] = 0
    request["username"] = support_steps.generate_random_letter_string(5)
    request["firstName"] = support_steps.generate_random_letter_string(6)
    request["lastName"] = support_steps.generate_random_letter_string(7)
    request["email"] = support_steps.generate_random_letter_string_mail(8)
    request["password"] = support_steps.generate_random_letter_string(5)
    request["phone"] = support_steps.generate_random_number_string(11)
    request["userStatus"] = support_steps.generate_random_number_string(5)
    # отправляем запрос
    request_post = requests.post(urls.url_user, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # отправляем запрос на удаление
    request_del = requests.delete(urls.url_user_get(str(request['email'])), verify=False)
    # проверяем ответ полученый на запрос
    print('view_request_delete = ', request_del)
    # проверяем что пользователь удален
    assert str(request_del).__contains__('404')

@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_get_user():
    # заполняем тело запроса
    request = {}
    request["id"] = 0
    request["username"] = support_steps.generate_random_letter_string(5)
    request["firstName"] = support_steps.generate_random_letter_string(6)
    request["lastName"] = support_steps.generate_random_letter_string(7)
    request["email"] = support_steps.generate_random_letter_string_mail(8)
    request["password"] = support_steps.generate_random_letter_string(5)
    request["phone"] = support_steps.generate_random_number_string(11)
    request["userStatus"] = support_steps.generate_random_number_string(5)
    # отправляем запрос
    request_post = requests.post(urls.url_user, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # вызываем get запрос
    request_get = requests.get(urls.url_user_get(str(request['username'])), verify=False)
    # получаем ответ
    print('view_result = ', json.dumps(request_get.json(), indent=4, sort_keys=True))
    # проверяем статус код
    assert str(request_get).__contains__('200')

@pytest.mark.full_regression
def test_get_user_negative():
    # заполняем тело запроса
    request = {}
    request["id"] = 0
    request["username"] = support_steps.generate_random_letter_string(5)
    request["firstName"] = support_steps.generate_random_letter_string(6)
    request["lastName"] = support_steps.generate_random_letter_string(7)
    request["email"] = support_steps.generate_random_letter_string_mail(8)
    request["password"] = support_steps.generate_random_letter_string(5)
    request["phone"] = support_steps.generate_random_number_string(11)
    request["userStatus"] = support_steps.generate_random_number_string(5)
    # отправляем запрос
    request_post = requests.post(urls.url_user, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # вызываем get запрос
    request_get = requests.get(urls.url_user_get(str(request['phone'])), verify=False)
    # получаем ответ
    print('view_result = ', json.dumps(request_get.json(), indent=4, sort_keys=True))
    # проверяем статус код и параметр message
    assert str(request_get).__contains__('404')
    assert request_get.json()['message'] == "User not found"

@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_put_user():
    # заполняем тело запроса
    request = {}
    request["id"] = 0
    request["username"] = support_steps.generate_random_letter_string(5)
    request["firstName"] = support_steps.generate_random_letter_string(6)
    request["lastName"] = support_steps.generate_random_letter_string(7)
    request["email"] = support_steps.generate_random_letter_string_mail(8)
    request["password"] = support_steps.generate_random_letter_string(5)
    request["phone"] = support_steps.generate_random_number_string(11)
    request["userStatus"] = support_steps.generate_random_number_string(5)
    # отправляем запрос
    request_post = requests.post(urls.url_user, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # заполняем тело запроса
    request_put = {}
    request_put["id"] = str(request_post.json()['message'])
    request_put["username"] = support_steps.generate_random_letter_string(5)
    request_put["firstName"] = support_steps.generate_random_letter_string(6)
    request_put["lastName"] = support_steps.generate_random_letter_string(7)
    request_put["email"] = support_steps.generate_random_letter_string_mail(8)
    request_put["password"] = support_steps.generate_random_letter_string(5)
    request_put["phone"] = support_steps.generate_random_number_string(11)
    request_put["userStatus"] = support_steps.generate_random_number_string(5)
    request_put_r = requests.put(urls.url_user_get(request["username"]), json=request_put, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_put = ', json.dumps(request_put_r.json(), indent=4, sort_keys=True))
    # проверяем статус код
    assert str(request_put_r).__contains__('200')
    # вызываем get запрос
    request_get = requests.get(urls.url_user_get(request_put['username']), verify=False)
    # получаем ответ
    print('view_result = ', json.dumps(request_get.json(), indent=4, sort_keys=True))
    # проверяем статус код и поле username
    assert str(request_get).__contains__('200')
    assert request_get.json()['username'] == request_put["username"]

@pytest.mark.full_regression
def test_put_user_negative():
    # заполняем тело запроса
    request = {}
    request["id"] = 0
    request["username"] = support_steps.generate_random_letter_string(5)
    request["firstName"] = support_steps.generate_random_letter_string(6)
    request["lastName"] = support_steps.generate_random_letter_string(7)
    request["email"] = support_steps.generate_random_letter_string_mail(8)
    request["password"] = support_steps.generate_random_letter_string(5)
    request["phone"] = support_steps.generate_random_number_string(11)
    request["userStatus"] = support_steps.generate_random_number_string(5)
    # отправляем запрос
    request_post = requests.post(urls.url_user, json=request, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_create = ', json.dumps(request_post.json(), indent=4, sort_keys=True))
    # заполняем тело запроса
    request_put = {}
    request_put["id"] = str(request_post.json()['message'])
    request_put["username"] = support_steps.generate_random_letter_string(5)
    request_put["firstName"] = support_steps.generate_random_letter_string(6)
    request_put["lastName"] = support_steps.generate_random_letter_string(7)
    request_put["email"] = support_steps.generate_random_letter_string_mail(8)
    request_put["password"] = support_steps.generate_random_letter_string(5)
    request_put["phone"] = support_steps.generate_random_number_string(11)
    request_put["userStatus"] = support_steps.generate_random_number_string(5)
    request_put_r = requests.put(urls.url_user_get(request["username"]), json=request_put, verify=False)
    # проверяем ответ полученый на запрос
    print('view_result_put = ', json.dumps(request_put_r.json(), indent=4, sort_keys=True))
    # проверяем статус код
    assert str(request_put_r).__contains__('200')
    # формируем пустое тело запроса
    request = {}
    #отправляем put запрос
    request_get = requests.get(urls.url_user_get(request_put["phone"]), json=request, verify=False)
    # Выводим содержимое ответа
    print('view = ', json.dumps(request_get.json(), indent=4, sort_keys=True))
    # проверяем что пользователь не найден
    assert str(request_get).__contains__('404')
    assert request_get.json()['message'] == 'User not found'