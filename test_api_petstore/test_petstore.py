import json
import requests
import pytest
import for_files
from resources import urls as urls
from Steps import support_steps as support_steps


def test_api():
    # задаем тело запроса
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем post запрос
    requests_post = requests.post(urls.url_pet, json=request, verify=False)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))

def test_post_pet():
    # наполняем тело запроса
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем post запрос
    requests_post = requests.post(urls.url_pet, json=request, verify=False)
    # выводим ответ в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выполняем проверку что id в теле ответа не пустой
    assert requests_post.json()['id'] is not None
    # отправляем get запрос по url заданным в предыдущем шаге
    request_get = requests.get(urls.url_pet_get(str(requests_post.json()['id'])), verify=False)
    # проверяем что значения параметра id в ответах на отправленные запросы совпадают
    assert requests_post.json()['id'] == request_get.json()['id']

def test_post_pet_negative():
    # задаем url и формируем тело запроса
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = []
    # отправляем post запрос
    requests_post = requests.post(urls.url_pet, json=request, verify=False)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выполняем проверку параметра message
    assert requests_post.json()['message'] == "something bad happened"

def test_get_pet():
    # задаем тело запроса
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем post запрос
    requests_post = requests.post(urls.url_pet, json=request, verify=False)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # отправляем get запрос
    request_get = requests.get(urls.url_pet_get(str(requests_post.json()['id'])), verify=False)
    # выводим результат запроса в формате json
    print("result=", json.dumps(request_get.json(), indent=4, sort_keys=True))
    # проверяем что id в url и ответе совпадают
    assert str(request_get.json()['id']) == str(requests_post.json()['id'])

def test_get_pet_negative():
    # задаем тело запроса
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем post запрос
    requests_post = requests.post(urls.url_pet, json=request, verify=False)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # отправляем get запрос с не существующим id
    request_get = requests.get(urls.url_pet_get(support_steps.generate_random_number_string(7)), verify=False)
    # выводим ответ на отправленный запрос в формате json
    print("result=", json.dumps(request_get.json(), indent=4, sort_keys=True))
    # выполняем проверку
    assert str(request_get).__contains__('404')

def test_put_pet():
    # заполняем тело запроса
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем составленный post запрос
    requests_post = requests.post(urls.url_pet, json=request, verify=False)
    # выводим ответ отправленного post запроса
    print('result_post=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # заполняем тело put запроса (url берем тот же)
    request_put = {}
    request_put['id'] = str(requests_post.json()['id'])
    request_put['name'] = support_steps.generate_random_letter_string(7)
    request_put['photoUrls'] = ['Photodog']
    # выведем тело сформированного post запроса для проверки
    print('request_put=', request_put)
    # отправим put запрос
    request_put_r = requests.put(urls.url_pet, json=request_put, verify=False)
    # выводим ответ отправленного put запроса
    print('result_put=', json.dumps(request_put_r.json(), indent=4, sort_keys=True))
    assert str(request_put_r.json()['name']) == request_put['name']

def test_del_pet():
    # отправим post запрос для создания сущности на удаление
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'

    requests_post = requests.post(urls.url_pet, json=request, verify=False)
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выполняем delete запрос и выводим результат запроса
    request_del = requests.delete(urls.url_pet_get(str(requests_post.json()['id'])), verify=False)
    print("result_del=", json.dumps(request_del.json(), indent=4, sort_keys=True))
    assert str(request_del).__contains__('200')

def test_put_pet_assert():
    # заполняем тело запроса
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем post запрос
    requests_post = requests.post(urls.url_pet, json=request, verify=False)
    # проверяем результат запроса
    print('result_post=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # создаем новое наполнение в тело запроса
    request_put = {}
    #  id берем с ответа на предыдущий запрос
    request_put['id'] = str(requests_post.json()['id'])
    request_put['name'] = support_steps.generate_random_letter_string(6)
    request_put['photoUrls'] = ['Photodog']
    #  отправляем put запрос
    request_put_r = requests.put(urls.url_pet, json=request_put, verify=False)
    #  проверяем ответ на запрос
    print('result_put=', json.dumps(request_put_r.json(), indent=4, sort_keys=True))
    # проверяем что данные изменились
    request_get = requests.get(urls.url_pet_get(str(requests_post.json()['id'])), verify=False)
    # проверяем что параметр name get запроса совпадает с параметром name put запроса
    assert request_get.json()['name'] == request_put['name']

def test_put_pet_negative():
    # заполняем тело запроса
    request_put = {}
    request_put['id'] = []
    request_put['name'] = support_steps.generate_random_letter_string(6)
    request_put['photoUrls'] = ['Photodog']
    # отправляем put запрос
    request_put_r = requests.put(urls.url_pet, json=request_put, verify=False)
    # проверяем ответ на запрос
    print('result_put=', json.dumps(request_put_r.json(), indent=4, sort_keys=True))
    # проверяем поле message
    assert request_put_r.json()['message'] == "something bad happened"


def test_delete_pet_negative():
    # сформируем и отправим post запрос для создания сущности
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'

    requests_post = requests.post(urls.url_pet, json=request, verify=False)
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # проверяем ответ
    assert str(requests_post).__contains__('200')
    # отправляем запрос
    request_del = requests.delete(urls.url_pet_get(support_steps.generate_random_letter_string(4)), verify=False)
    # выводим результат запроса
    print("result_del=", json.dumps(request_del.json(), indent=4, sort_keys=True))
    # проверяем ответ
    assert str(request_del).__contains__('404')


def test_post_image():
    # сформируем и отправим post запрос для создания сущности
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = ['photoDog']
    request['category'] = {}
    request['category']['name'] = 'dogs'
    requests_post = requests.post(urls.url_pet, json=request, verify=False)
    print('result_post=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # откроем файл для чтения
    file = for_files.open_file('venv/Scripts/files/send.txt')
    # отправляем post запрос с аттачем
    post_file = requests.post(urls.url_pet_upload(str(requests_post.json()['id'])), files=file, verify=False)
    # выводим url на который отправили запрос для проверки сформированного id, и проверяем ответ на запрос
    print('response = ', urls.url_pet_upload(str(requests_post.json()['id'])), post_file)
    # закрываем файл
    for_files.close_file(file)
    # Проверка ответа на загрузку post запроса с аттачем
    assert post_file.json()['code'] is not None

def test_post_image_negative():
    # сформируем и отправим post запрос для создания сущности
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = ['photoDog']
    request['category'] = {}
    request['category']['name'] = 'dogs'

    requests_post = requests.post(urls.url_pet, json=request, verify=False)
    print('result_post=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # сформируем post запрос для отправки без аттача с id ответа на прошлый запрос
    # отправляем запрос
    post_file = requests.post(urls.url_pet_upload(str(requests_post.json()['id'])), verify=False)
    # выводим url для проверки id и ответ который пришел
    print('response = ', urls.url_pet_upload(str(requests_post.json()['id'])), post_file)
    # Проверка ответа на загрузку post запроса с аттачем
    assert str(post_file).__contains__("415")

def test_post_pet_update():
    # заполняем тело запроса
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем post запрос
    requests_post = requests.post(urls.url_pet, json=request, verify=False)
    # выводим ответ в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выполняем проверку что id в теле ответа не пустой
    assert requests_post.json()['id'] is not None
    # наполняем тело запроса
    name = support_steps.generate_random_letter_string(6)
    status = support_steps.generate_random_letter_string(6)
    form_data = 'name=' + name + '&' + 'status=' + status
    # отправляем запрос
    request_update_post = requests.post(urls.url_pet_get(str(requests_post.json()['id'])), data=form_data, verify=False)
    # Выводим ответ на запрос
    print('update=', json.dumps(request_update_post.json(), indent=4, sort_keys=True))
    # проверка на ошибку
    assert str(request_update_post).__contains__('200')
    # для проверки изменений отправим get запрос с id указаным в ответе первого запроса
    request_get = requests.get(urls.url_pet_get(str(requests_post.json()['id'])), verify=False)
    # выводим результа get запроса
    print('get request = ', json.dumps(request_get.json(), indent=4, sort_keys=True))
    # проверим что тело ответа на get запрос совпадает с телом отправленным в post запросе на изменения
    assert str(request_get).__contains__('200')
    assert request_get.json()['name'] == name
    assert request_get.json()['status'] == status

def test_post_pet_update_negative():
    # заполняем тело запроса
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем post запрос
    requests_post = requests.post(urls.url_pet, json=request, verify=False)
    # выводим ответ в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выполняем проверку что id в теле ответа не пустой
    assert requests_post.json()['id'] is not None
    # задаем url запроса, указываем не существующий id
    # наполняем тело запроса
    name = support_steps.generate_random_letter_string(6)
    status = support_steps.generate_random_letter_string(6)
    form_data = 'name=' + name + '&' + 'status=' + status
    # отправляем запрос
    request_update_post = requests.post(urls.url_pet_get(support_steps.generate_random_number_string(9)), data=form_data, verify=False)
    # Выводим ответ на запрос
    print('update=', json.dumps(request_update_post.json(), indent=4, sort_keys=True))
    # проверка на ошибку
    assert str(request_update_post).__contains__('404')
    assert request_update_post.json()['message'] == "not found"

def test_find_by_status():
    # задаем тело запроса
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    request['status'] = 'available'
    # отправляем post запрос
    requests_post = requests.post(urls.url_pet, json=request, verify=False)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # отправляем get запрос
    request_get = requests.get(urls.url_pet_find_by_status('available'), verify=False)
    # выводим ответ в формате json
    print('result get=', json.dumps(request_get.json(), indent=4, sort_keys=True))
    #выполняем проверку на статус код и что массив не пуст
    assert str(request_get).__contains__('200')
    assert request_get.json() != []

def test_find_by_status_negative():
    # задаем тело запроса
    request = {}
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    request['status'] = 'available'
    # отправляем post запрос
    requests_post = requests.post(urls.url_pet, json=request, verify=False)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выводим ответ в формате json
    request_get = requests.get(urls.url_pet_find_by_status('open'), verify=False)
    print('result get=', json.dumps(request_get.json(), indent=4, sort_keys=True))
    # выполняем проверку на статус код и что массив пуст
    assert request_get.json() == []

