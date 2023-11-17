import json
import pytest
import for_files
import allure
from resources import urls as urls
from Steps import support_steps as support_steps
from Steps import generate_json_steps as generate_json_steps
from Steps import request_steps as request_steps
from Steps import assert_steps as assert_steps

@allure.step
@pytest.mark.smoke_regression
@pytest.mark.full_regression
# Создание питомца
def test_api():
    # задаем тело запроса
    request = generate_json_steps.create_json_post_pet_required_params(support_steps.generate_random_number_string(11))
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))

@allure.step
@pytest.mark.smoke_regression
@pytest.mark.full_regression
@pytest.mark.parametrize(
    'type',
    [
        (generate_json_steps.create_json_post_pet_required_params(support_steps.generate_random_number_string(11))),
        (generate_json_steps.create_json_post_pet_all_params(support_steps.generate_random_number_string(11), 'available'))
    ],
    ids=["required params", "all params"]
)
# Создание питомца с проверкой на совпадение по id
def test_post_pet(type):
    # задаем тело запроса с передоваемым типом
    request = type
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # выводим ответ в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выполняем проверку что id в теле ответа не пустой
    assert_steps.assert_not_none_id(requests_post)
    # отправляем get запрос по url заданным в предыдущем шаге
    request_get = request_steps.request_get(urls.url_pet_get(str(requests_post.json()['id'])))
    # проверяем что значения параметра id в ответах на отправленные запросы совпадают
    assert_steps.assert_equals_response_ids(request_get, requests_post)

@pytest.mark.negative_tests
@pytest.mark.full_regression
# Негативный сценарий создания питомца с проверкой на совпадение по id
def test_post_pet_negative():
    # задаем url и формируем тело запроса
    request = generate_json_steps.create_json_post_pet_all_params([], None)
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выполняем проверку параметра message
    assert_steps.assert_not_correct_message(requests_post, "something bad happened")

@pytest.mark.smoke_regression
@pytest.mark.full_regression
# Проверка питомца по id
def test_get_pet():
    # задаем тело запроса
    request = generate_json_steps.create_json_post_pet_all_params(support_steps.generate_random_number_string(11), 'available')
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # отправляем get запрос
    request_get = request_steps.request_get(urls.url_pet_get(str(requests_post.json()['id'])))
    # выводим результат запроса в формате json
    print("result=", json.dumps(request_get.json(), indent=4, sort_keys=True))
    # проверяем что id в url и ответе совпадают
    assert_steps.assert_equals_response_ids(requests_post, request_get)

@pytest.mark.negative_tests
@pytest.mark.full_regression
# Негативный сценарий проверки питомца по id
def test_get_pet_negative():
    # задаем тело запроса
    request = generate_json_steps.create_json_post_pet_required_params(support_steps.generate_random_number_string(11))
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # отправляем get запрос с не существующим id
    request_get = request_steps.request_get(urls.url_pet_get(support_steps.generate_random_number_string(7)))
    # выводим ответ на отправленный запрос в формате json
    print("result=", json.dumps(request_get.json(), indent=4, sort_keys=True))
    # выполняем проверку
    assert_steps.assert_status_code(request_get, '404')

@pytest.mark.smoke_regression
@pytest.mark.full_regression
# Редактирование анкеты питомца
def test_put_pet():
    # заполняем тело запроса
    request = generate_json_steps.create_json_post_pet_required_params(support_steps.generate_random_number_string(11))
    # отправляем составленный post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # выводим ответ отправленного post запроса
    print('result_post=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # заполняем тело put запроса (url берем тот же)
    request_put = generate_json_steps.create_json_post_pet_required_params(str(requests_post.json()['id']))
    # выведем тело сформированного post запроса для проверки
    print('request_put=', request_put)
    # отправим put запрос
    request_put_r = request_steps.request_put(urls.url_pet, request_put)
    # выводим ответ отправленного put запроса
    print('result_put=', json.dumps(request_put_r.json(), indent=4, sort_keys=True))
    assert_steps.assert_equals_response_params(request_put_r, request_put)

@pytest.mark.smoke_regression
@pytest.mark.full_regression
# Удаление питомца
def test_del_pet():
    # отправим post запрос для создания сущности на удаление
    request = generate_json_steps.create_json_post_pet_all_params(support_steps.generate_random_number_string(11), 'available')
    requests_post = request_steps.request_post(urls.url_pet, request)
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выполняем delete запрос
    request_del = request_steps.request_delete(urls.url_pet_get(str(requests_post.json()['id'])))
    # выводим результат запроса
    print("result_del=", json.dumps(request_del.json(), indent=4, sort_keys=True))
    # проверка ответа
    assert_steps.assert_status_code(request_del, '200')

@allure.step
@pytest.mark.full_regression
# Редактирование анкеты питомца с проверкой внесенных изменений get запросом
def test_put_pet_assert():
    # заполняем тело запроса
    request = generate_json_steps.create_json_post_pet_all_params(support_steps.generate_random_number_string(11), 'available')
    # отправляем post запрос
    print(("id", request))
    requests_post = request_steps.request_post(urls.url_pet, request)
    # проверяем результат запроса
    print('result_post=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # создаем новое наполнение в тело запроса
    # заполняем тело put запроса (url берем тот же)
    request_put = generate_json_steps.create_json_post_pet_all_params(str(requests_post.json()['id']), 'available')
    # выведем тело сформированного post запроса для проверки
    print('request_put=', request_put)
    # отправим put запрос
    request_put_r = request_steps.request_put(urls.url_pet, request_put)
    # выводим ответ отправленного put запроса
    print('result_put=', json.dumps(request_put_r.json()['id'], indent=4, sort_keys=True))
    assert_steps.assert_equals_response_params(request_put_r, request_put)
    # проверяем что данные изменились
    request_get = request_steps.request_get(urls.url_pet_get(str(request_put_r.json()['id'])))
    # проверяем что параметр name get запроса совпадает с параметром name put запроса
    assert_steps.assert_equals_response_params_name(request_get, request_put_r)

@pytest.mark.negative_tests
@pytest.mark.full_regression
# Негативный сценарий изменения данных о питомце
def test_put_pet_negative():
    # заполняем тело запроса
    request = generate_json_steps.create_json_post_pet_all_params([], None)
    # отправляем put запрос
    request_put = request_steps.request_post(urls.url_pet, request)
    # проверяем ответ на запрос
    print('result_put=', json.dumps(request_put.json(), indent=4, sort_keys=True))
    # проверяем поле message
    assert_steps.assert_not_correct_message(request_put, "something bad happened")

@allure.step
@pytest.mark.negative_tests
@pytest.mark.full_regression
# Негативный сценарий удаления питомца
def test_delete_pet_negative():
    # сформируем и отправим post запрос для создания сущности
    request = generate_json_steps.create_json_post_pet_all_params(support_steps.generate_random_number_string(11), 'available')
    requests_post = request_steps.request_post(urls.url_pet, request)
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # проверяем ответ
    assert_steps.assert_status_code(requests_post, '200')
    # отправляем запрос c невалидным id
    request_del = request_steps.request_delete(urls.url_pet_get(support_steps.generate_random_letter_string(4)))
    # выводим результат запроса
    print("result_del=", json.dumps(request_del.json(), indent=4, sort_keys=True))
    # проверяем ответ
    assert_steps.assert_status_code(request_del, '404')


@pytest.mark.smoke_regression
@pytest.mark.full_regression
@pytest.mark.parametrize(
    'type',
    [
        (generate_json_steps.create_json_post_pet_required_params(support_steps.generate_random_number_string(11))),
        (generate_json_steps.create_json_post_pet_all_params(support_steps.generate_random_number_string(11), 'available'))
    ],
    ids=["required params", "all params"]
)
# Проверка отправки аттачментов к анкете питомца
def test_post_image(type):
    # сформируем и отправим post запрос для создания сущности
    request = type
    requests_post = request_steps.request_post(urls.url_pet, request)
    print('result_post=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # откроем файл для чтения
    file = for_files.open_file('C:/Users/19787543/PycharmProjects/cource_python/test_api_petstore/venv/Scripts/files/send.txt')
    # отправляем post запрос с аттачем
    post_file = request_steps.request_file(urls.url_pet_upload(str(requests_post.json()['id'])), file)
    # выводим url на который отправили запрос для проверки сформированного id, и проверяем ответ на запрос
    print('response = ', urls.url_pet_upload(str(requests_post.json()['id'])), post_file)
    # закрываем файл
    for_files.close_file(file)
    # Проверка ответа на загрузку post запроса с аттачем
    assert_steps.assert_is_not_none(post_file, 'code')

@pytest.mark.negative_tests
@pytest.mark.full_regression
# Негативный сценарий проверки аттачментов к анкете питомца
def test_post_image_negative():
    # сформируем и отправим post запрос для создания сущности
    request = generate_json_steps.create_json_post_pet_all_params(support_steps.generate_random_number_string(11), 'available')
    requests_post = request_steps.request_post(urls.url_pet, request)
    print('result_post=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # сформируем post запрос для отправки без аттача с id ответа на прошлый запрос
    # отправляем запрос
    post_file = request_steps.request_post(urls.url_pet_upload(str(requests_post.json()['id'])), request)
    # выводим url для проверки id и ответ который пришел
    print('response = ', urls.url_pet_upload(str(requests_post.json()['id'])), post_file)
    # Проверка ответа на загрузку post запроса с аттачем
    assert_steps.assert_status_code(post_file, '415')

@pytest.mark.smoke_regression
@pytest.mark.full_regression
@pytest.mark.parametrize(
    'type',
    [
        (generate_json_steps.create_json_post_pet_required_params(support_steps.generate_random_number_string(11))),
        (generate_json_steps.create_json_post_pet_all_params(support_steps.generate_random_number_string(11), 'available'))
    ],
    ids=["required param", "all param"]
)
# Проверка изменения параметров в анкете питомца
def test_post_pet_update(type):
    # заполняем тело запроса
    request = type
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # выводим ответ в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выполняем проверку что id в теле ответа не пустой
    assert_steps.assert_status_code(requests_post, '200')
    # наполняем тело запроса
    name = support_steps.generate_random_letter_string(6)
    status = support_steps.generate_random_letter_string(6)
    form_data = 'name=' + name + '&' + 'status=' + status
    # отправляем запрос
    request_update_post = request_steps.request_data(urls.url_pet_get(str(requests_post.json()['id'])), form_data)
    # Выводим ответ на запрос
    print('update=', json.dumps(request_update_post.json(), indent=4, sort_keys=True))
    # проверка на ошибку
    assert_steps.assert_status_code(request_update_post, '200')
    # для проверки изменений отправим get запрос с id указаным в ответе первого запроса
    request_get = request_steps.request_get(urls.url_pet_get(str(requests_post.json()['id'])))
    # выводим результа get запроса
    print('get request = ', json.dumps(request_get.json(), indent=4, sort_keys=True))
    # проверим что тело ответа на get запрос совпадает с телом отправленным в post запросе на изменения
    assert_steps.assert_status_code(request_get, '200')
    assert_steps.assert_equals_params(request_get, 'name', name)
    assert_steps.assert_equals_params(request_get, 'status', status)

@pytest.mark.negative_tests
@pytest.mark.full_regression
# Негативный сценарий проверки изменения параметров в анкете питомца
def test_post_pet_update_negative():
    # заполняем тело запроса
    request = generate_json_steps.create_json_post_pet_all_params(support_steps.generate_random_number_string(11), 'available')
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # выводим ответ в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выполняем проверку что id в теле ответа не пустой
    assert_steps.assert_status_code(requests_post, '200')
    # задаем url запроса, указываем не существующий id
    # наполняем тело запроса
    name = support_steps.generate_random_letter_string(6)
    status = support_steps.generate_random_letter_string(6)
    form_data = 'name=' + name + '&' + 'status=' + status
    # отправляем запрос
    request_update_post = request_steps.request_data(urls.url_pet_get(support_steps.generate_random_number_string(9)), form_data)
    # Выводим ответ на запрос
    print('update=', json.dumps(request_update_post.json(), indent=4, sort_keys=True))
    # проверка на ошибку
    assert_steps.assert_status_code(request_update_post, '404')

@pytest.mark.smoke_regression
@pytest.mark.full_regression
@pytest.mark.parametrize(
    'type',
    [
        (generate_json_steps.create_json_post_pet_all_params(support_steps.generate_random_number_string(11), "available")),
        (generate_json_steps.create_json_post_pet_all_params(support_steps.generate_random_number_string(11), "pending")),
        (generate_json_steps.create_json_post_pet_all_params(support_steps.generate_random_number_string(11), "sold"))
    ],
    ids=["status available", "status pending", "status sold"]
)
# Проверка получения анкеты питомца по статусу
def test_find_by_status(type):
    # задаем тело запроса
    request = type
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # отправляем get запрос
    request_get = request_steps.request_get(urls.url_for_find(requests_post))
    print('result get=', json.dumps(request_get.json(), indent=4, sort_keys=True))
    #выполняем проверку на статус код и что массив не пуст
    assert_steps.assert_status_code(request_get, '200')
    assert_steps.assert_massive(request_get)

@pytest.mark.negative_tests
@pytest.mark.full_regression
@pytest.mark.parametrize(
    'type',
    [
        (generate_json_steps.create_json_post_pet_all_params(support_steps.generate_random_number_string(11), "available")),
        (generate_json_steps.create_json_post_pet_all_params(support_steps.generate_random_number_string(11), "pending")),
        (generate_json_steps.create_json_post_pet_all_params(support_steps.generate_random_number_string(11), "sold"))
    ],
    ids=["status available", "status pending", "status sold"]
)
# Негативный сценарий проверки получения анкеты питомца по статусу
def test_find_by_status_negative(type):
    # Задаем тело запроса
    request = type
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выводим ответ в формате json
    request_get = request_steps.request_get(urls.url_pet_find_by_status('open'))
    print('result get=', json.dumps(request_get.json(), indent=4, sort_keys=True))
    # выполняем проверку на статус код и что массив пуст
    assert_steps.assert_massive_null(request_get)

