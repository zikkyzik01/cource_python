import pytest
import requests
import json
from resources import urls as urls
from Steps import support_steps as support_steps
from Steps import generate_json_steps as generate_json_steps
from Steps import request_steps as request_steps
from Steps import assert_steps as assert_steps

@pytest.mark.smoke_regression
@pytest.mark.full_regression
@pytest.mark.parametrize(
    'type',
    [
        (generate_json_steps.create_json_post_user_all_params()),
        (generate_json_steps.create_json_post_user_not_params())
    ],
    ids=["with params", "none params"]
)
# Создание пользователя
def test_create_user(type):
    # заполняем тело запроса
    request = type
    # отправляем запрос
    request_post = request_steps.request_post(urls.url_user, request)
    # проверяем что статус код ответа 200
    assert_steps.assert_status_code(request_post, '200')

@pytest.mark.negative_tests
@pytest.mark.full_regression
# Негативный сценарий создания пользователя
def test_create_user_negative():
    # заполняем тело запроса
    request = generate_json_steps.create_json_post_user_all_params()
    request["userStatus"] = support_steps.generate_random_number_string(13)
    # отправляем запрос
    request_post = request_steps.request_post(urls.url_user, request)
    # проверяем что статус код ответа 500, и параметр message
    assert_steps.assert_status_code(request_post, '500')
    assert_steps.assert_not_correct_message(request_post, "something bad happened")

@pytest.mark.smoke_regression
@pytest.mark.full_regression
# Удаление пользователя
def test_delete_user():
    # заполняем тело запроса
    request = generate_json_steps.create_json_post_user_all_params()
    # отправляем post запрос
    request_steps.request_post(urls.url_user, request)
    # отправляем запрос на удаление
    request_del = request_steps.request_delete(urls.url_user_get(request['username']))
    # проверяем что пользователь удален
    assert_steps.assert_status_code(request_del, '200')

@pytest.mark.negative_tests
@pytest.mark.full_regression
# Негативный сценарий удаления пользователя
def test_delete_user_negative():
    # заполняем тело запроса
    request = generate_json_steps.create_json_post_user_all_params()
    # отправляем запрос
    response_del = request_steps.request_post(urls.url_user, request)
    # отправляем запрос на удаление
    request_del = request_steps.request_delete(urls.url_user_get(str(request['email'])))
    # проверяем что пользователь удален
    assert_steps.assert_status_code(request_del, '404')

@pytest.mark.smoke_regression
@pytest.mark.full_regression
#  Получение информации о созданном пользователе
def test_get_user():
    # заполняем тело запроса
    request = generate_json_steps.create_json_post_user_all_params()
    # отправляем запрос
    request_post = request_steps.request_post(urls.url_user, request)
    # вызываем get запрос
    request_get = request_steps.request_get(urls.url_user_get(str(request['username'])))
    # проверяем статус код
    assert_steps.assert_status_code(request_get, '200')

@pytest.mark.negative_tests
@pytest.mark.full_regression
# Негативный сценарий получения информации о созданном пользователе
def test_get_user_negative():
    # заполняем тело запроса
    request = generate_json_steps.create_json_post_user_all_params()
    # отправляем запрос
    request_post = request_steps.request_post(urls.url_user, request)
    # вызываем get запрос
    request_get = request_steps.request_get(urls.url_user_get(str(request['phone'])))
    # проверяем статус код и параметр message
    assert_steps.assert_status_code(request_get, '404')
    assert_steps.assert_not_correct_message(request_get, "User not found")

@pytest.mark.smoke_regression
@pytest.mark.full_regression
# Изменение пользователя
def test_put_user():
    # заполняем тело запроса
    request = generate_json_steps.create_json_post_user_all_params()
    # отправляем запрос
    request_post = request_steps.request_post(urls.url_user, request)
    # заполняем тело запроса
    request_put = generate_json_steps.create_json_post_user_all_params()
    request_put['message'] = request_post.json()['message']
    # отправляем запрос
    request_put_r = request_steps.request_put(urls.url_user_get(request["username"]), request_put)
    # проверяем статус код
    assert_steps.assert_status_code(request_put_r, '200')
    # вызываем get запрос
    request_get = request_steps.request_get(urls.url_user_get(request_put['username']))
    # проверяем статус код и поле username
    assert_steps.assert_status_code(request_get, '200')
    assert_steps.assert_equals_response_params_username(request_get, request_put)

@pytest.mark.negative_tests
@pytest.mark.full_regression
#  Негативный сценарий изменения пользователя
def test_put_user_negative():
    # заполняем тело запроса
    request = generate_json_steps.create_json_post_user_all_params()
    # отправляем запрос
    request_post = request_steps.request_post(urls.url_user, request)
    # заполняем тело запроса
    request_put = generate_json_steps.create_json_post_user_all_params()
    request_put['message'] = request_post.json()['message']
    # отправляем запрос
    request_put_r = request_steps.request_put(urls.url_user_get(request["username"]), request_put)
    # проверяем статус код
    assert_steps.assert_status_code(request_put_r, '200')
    #отправляем get запрос c невалидными данными
    request_get = request_steps.request_get(urls.url_user_get(request_put["phone"]))
    # проверяем что пользователь не найден
    assert_steps.assert_status_code(request_get, '404')
    assert_steps.assert_not_correct_message(request_get, "User not found")