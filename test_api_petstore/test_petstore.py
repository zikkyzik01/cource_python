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
    request = generate_json_steps.create_json_post_pet_required_params()
    # отправляем post запрос
    request_steps.request_post(urls.url_pet, request)

@allure.step
@pytest.mark.smoke_regression
@pytest.mark.full_regression
@pytest.mark.parametrize(
    'type',
    [
        (generate_json_steps.create_json_post_pet_required_params()),
        (generate_json_steps.create_json_post_pet_all_params())
    ],
    ids=["required params", "all params"]
)
# Создание питомца с проверкой на совпадение по id
def test_post_pet(type):
    # задаем тело запроса с передоваемым типом
    request = type
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
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
    request = generate_json_steps.create_json_post_pet_all_params()
    request['name']=[]
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # выполняем проверку параметра message
    assert_steps.assert_not_correct_message(requests_post, "something bad happened")

@pytest.mark.smoke_regression
@pytest.mark.full_regression
# Проверка питомца по id
def test_get_pet():
    # задаем тело запроса
    request = generate_json_steps.create_json_post_pet_all_params()
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # отправляем get запрос
    request_get = request_steps.request_get(urls.url_pet_get(str(requests_post.json()['id'])))
    # проверяем что id в url и ответе совпадают
    assert_steps.assert_equals_response_ids(requests_post, request_get)

@pytest.mark.negative_tests
@pytest.mark.full_regression
# Негативный сценарий проверки питомца по id
def test_get_pet_negative():
    # задаем тело запроса
    request = generate_json_steps.create_json_post_pet_required_params()
    # отправляем post запрос
    request_steps.request_post(urls.url_pet, request)
    # отправляем get запрос с не существующим id
    request_get = request_steps.request_get(urls.url_pet_get(support_steps.generate_random_number_string(7)))
    # выполняем проверку
    assert_steps.assert_status_code(request_get, '404')

@pytest.mark.smoke_regression
@pytest.mark.full_regression
# Редактирование анкеты питомца
def test_put_pet():
    # заполняем тело запроса
    request = generate_json_steps.create_json_post_pet_required_params()
    # отправляем составленный post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # заполняем тело put запроса (url берем тот же)
    request_put = generate_json_steps.create_json_post_pet_required_params()
    request_put['id'] = str(requests_post.json()['id'])
    # отправим put запрос
    request_put_r = request_steps.request_put(urls.url_pet, request_put)
    assert_steps.assert_equals_response_params(request_put_r, request_put)

@pytest.mark.smoke_regression
@pytest.mark.full_regression
# Удаление питомца
def test_del_pet():
    # отправим post запрос для создания сущности на удаление
    request = generate_json_steps.create_json_post_pet_all_params()
    requests_post = request_steps.request_post(urls.url_pet, request)
    # выполняем delete запрос
    request_del = request_steps.request_delete(urls.url_pet_get(str(requests_post.json()['id'])))
    # проверка ответа
    assert_steps.assert_status_code(request_del, '200')

@allure.step
@pytest.mark.full_regression
# Редактирование анкеты питомца с проверкой внесенных изменений get запросом
def test_put_pet_assert():
    # заполняем тело запроса
    request = generate_json_steps.create_json_post_pet_all_params()
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # создаем новое наполнение в тело запроса (url берем c ответа первого шага)
    request_put = generate_json_steps.create_json_post_pet_all_params()
    request_put['id'] = str(requests_post.json()['id'])
    # отправим put запрос
    request_put_r = request_steps.request_put(urls.url_pet, request_put)
    # проверяем ответ отправленного put запроса
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
    request = generate_json_steps.create_json_post_pet_all_params()
    request['name'] = []
    # отправляем put запрос
    request_put = request_steps.request_post(urls.url_pet, request)
    # проверяем поле message
    assert_steps.assert_not_correct_message(request_put, "something bad happened")

@allure.step
@pytest.mark.negative_tests
@pytest.mark.full_regression
# Негативный сценарий удаления питомца
def test_delete_pet_negative():
    # сформируем и отправим post запрос для создания сущности
    request = generate_json_steps.create_json_post_pet_all_params()
    requests_post = request_steps.request_post(urls.url_pet, request)
    # проверяем ответ
    assert_steps.assert_status_code(requests_post, '200')
    # отправляем запрос c невалидным id
    request_del = request_steps.request_delete(urls.url_pet_get(support_steps.generate_random_letter_string(4)))
    # проверяем ответ
    assert_steps.assert_status_code(request_del, '404')


@pytest.mark.smoke_regression
@pytest.mark.full_regression
@pytest.mark.parametrize(
    'type',
    [
        (generate_json_steps.create_json_post_pet_required_params()),
        (generate_json_steps.create_json_post_pet_all_params())
    ],
    ids=["required params", "all params"]
)
# Проверка отправки аттачментов к анкете питомца
def test_post_image(type):
    # сформируем и отправим post запрос для создания сущности
    request = type
    requests_post = request_steps.request_post(urls.url_pet, request)
    # откроем файл для чтения
    file = for_files.open_file('venv/Scripts/files/send.txt')
    # отправляем post запрос с аттачем
    post_file = request_steps.request_file(urls.url_pet_upload(str(requests_post.json()['id'])), file)
    # закрываем файл
    for_files.close_file(file)
    # Проверка ответа на загрузку post запроса с аттачем
    assert_steps.assert_is_not_none(post_file, 'code')

@pytest.mark.negative_tests
@pytest.mark.full_regression
# Негативный сценарий проверки аттачментов к анкете питомца
def test_post_image_negative():
    # сформируем и отправим post запрос для создания сущности
    request = generate_json_steps.create_json_post_pet_all_params()
    requests_post = request_steps.request_post(urls.url_pet, request)
    # сформируем post запрос для отправки без аттача с id ответа на прошлый запрос
    # отправляем запрос
    post_file = request_steps.request_file(urls.url_pet_upload(str(requests_post.json()['id'])), None)
    # Проверка ответа на загрузку post запроса с аттачем
    assert_steps.assert_status_code(post_file, '415')

@pytest.mark.smoke_regression
@pytest.mark.full_regression
@pytest.mark.parametrize(
    'type',
    [
        (generate_json_steps.create_json_post_pet_required_params()),
        (generate_json_steps.create_json_post_pet_all_params())
    ],
    ids=["required param", "all param"]
)
# Проверка изменения параметров в анкете питомца
def test_post_pet_update(type):
    # заполняем тело запроса
    request = type
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # выполняем проверку что id в теле ответа не пустой
    assert_steps.assert_status_code(requests_post, '200')
    # наполняем тело запроса
    name = support_steps.generate_random_letter_string(6)
    status = support_steps.generate_random_letter_string(6)
    form_data = 'name=' + name + '&' + 'status=' + status
    # отправляем запрос
    request_update_post = request_steps.request_data(urls.url_pet_get(str(requests_post.json()['id'])), form_data)
    # проверка на ошибку
    assert_steps.assert_status_code(request_update_post, '200')
    # для проверки изменений отправим get запрос с id указаным в ответе первого запроса
    request_get = request_steps.request_get(urls.url_pet_get(str(requests_post.json()['id'])))
    # проверим что тело ответа на get запрос совпадает с телом отправленным в post запросе на изменения
    assert_steps.assert_status_code(request_get, '200')
    assert_steps.assert_equals_params(request_get, 'name', name)
    assert_steps.assert_equals_params(request_get, 'status', status)

@pytest.mark.negative_tests
@pytest.mark.full_regression
# Негативный сценарий проверки изменения параметров в анкете питомца
def test_post_pet_update_negative():
    # заполняем тело запроса
    request = generate_json_steps.create_json_post_pet_all_params()
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # выполняем проверку что id в теле ответа не пустой
    assert_steps.assert_status_code(requests_post, '200')
    # задаем url запроса, указываем не существующий id
    name = support_steps.generate_random_letter_string(6)
    status = support_steps.generate_random_letter_string(6)
    form_data = 'name=' + name + '&' + 'status=' + status
    # отправляем запрос
    request_update_post = request_steps.request_data(urls.url_pet_get(support_steps.generate_random_number_string(9)), form_data)
    # проверка на ошибку
    assert_steps.assert_status_code(request_update_post, '404')

@pytest.mark.smoke_regression
@pytest.mark.full_regression
# Проверка получения анкеты питомца по статусу
def test_find_by_status():
    # задаем тело запроса
    request = generate_json_steps.create_json_post_pet_all_params()
    request['status'] = 'available'
    # отправляем post запрос со статусом available
    response_status_available = request_steps.request_post(urls.url_pet, request)
    # отправляем get запрос
    request_get_available = request_steps.request_get(urls.url_pet_find_by_status(response_status_available.json()['status']))
    # выполняем проверку на статус код и что массив не пуст
    assert_steps.assert_status_code(request_get_available, '200')
    assert_steps.assert_massive(request_get_available)
    # отправляем post запрос со статусом pending
    request['status'] = 'pending'
    response_status_pending = request_steps.request_post(urls.url_pet, request)
    # отправляем get запрос
    request_get_pending = request_steps.request_get(urls.url_pet_find_by_status(response_status_pending.json()['status']))
    # выполняем проверку на статус код и что массив не пуст
    assert_steps.assert_status_code(request_get_pending, '200')
    assert_steps.assert_massive(request_get_pending)
    # отправляем post запрос со статусом sold
    request['status'] = 'sold'
    response_status_sold = request_steps.request_post(urls.url_pet, request)
    # отправляем get запрос
    request_get_sold = request_steps.request_get(urls.url_pet_find_by_status(response_status_sold.json()['status']))
    #выполняем проверку на статус код и что массив не пуст
    assert_steps.assert_status_code(request_get_sold, '200')
    assert_steps.assert_massive(request_get_sold)

@pytest.mark.negative_tests
@pytest.mark.full_regression
# Негативный сценарий проверки получения анкеты питомца по статусу
def test_find_by_status_negative():
    # Задаем тело запроса
    request = generate_json_steps.create_json_post_pet_all_params()
    # отправляем post запрос
    requests_post = request_steps.request_post(urls.url_pet, request)
    # выводим ответ в формате json
    request_get = request_steps.request_get(urls.url_pet_find_by_status(support_steps.generate_random_letter_string(5)))
    # выполняем проверку на статус код и что массив пуст
    assert_steps.assert_massive_null(request_get)

