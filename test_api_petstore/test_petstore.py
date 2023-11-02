import json
import requests
import pytest
import for_files


def test_api():
    # задаем url
    url = "https://petstore.swagger.io/v2/pet"
    # задаем тело запроса
    request = {}
    request['name'] = 'sbercat'
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем post запрос
    requests_post = requests.post(url, json=request, verify=False)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))

def test_post_pet():
    # задаем url и наполняем тело запроса
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = 'sbercat'
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем post запрос
    requests_post = requests.post(url, json=request, verify=False)
    # выводим ответ в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выполняем проверку что id в теле ответа не пустой
    assert requests_post.json()['id'] is not None
    # задаем url запроса, берем id из ответа предыдущего шага
    url_get = "https://petstore.swagger.io/v2/pet/" + str(requests_post.json()['id'])
    # отправляем get запрос по url заданным в предыдущем шаге
    request_get = requests.get(url_get, verify=False)
    # проверяем что значения параметра id в ответах на отправленные запросы совпадают
    assert requests_post.json()['id'] == request_get.json()['id']

def test_post_pet_negative():
    # задаем url и формируем тело запроса
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = 'sbercat'
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = []
    # отправляем post запрос
    requests_post = requests.post(url, json=request, verify=False)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выполняем проверку параметра message
    assert requests_post.json()['message'] == "something bad happened"

def test_get_pet():
    # задаем url
    url = "https://petstore.swagger.io/v2/pet"
    # задаем тело запроса
    request = {}
    request['name'] = 'sbercat'
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем post запрос
    requests_post = requests.post(url, json=request, verify=False)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # задаем url
    url_get = "https://petstore.swagger.io/v2/pet/" + str(requests_post.json()['id'])
    # отправляем get запрос
    request_get = requests.get(url_get, verify=False)
    # выводим результат запроса в формате json
    print("result=", json.dumps(request_get.json(), indent=4, sort_keys=True))
    # проверяем что id в url и ответе совпадают
    assert str(request_get.json()['id']) == str(requests_post.json()['id'])

def test_get_pet_negative():
    # задаем url
    url = "https://petstore.swagger.io/v2/pet"
    # задаем тело запроса
    request = {}
    request['name'] = 'sbercat'
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем post запрос
    requests_post = requests.post(url, json=request, verify=False)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # задаем не корректный url и отправляем get запрос
    url_get = "https://petstore.swagger.io/v2/pet/" + 'petcat'
    request_get = requests.get(url_get, verify=False)
    # выводим ответ на отправленный запрос в формате json
    print("result=", json.dumps(request_get.json(), indent=4, sort_keys=True))
    # выполняем проверку
    assert str(request_get).__contains__('404')

def test_put_pet():
    # задаем url и заполняем тело запроса
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = 'sbercat'
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем составленный post запрос
    requests_post = requests.post(url, json=request, verify=False)
    # выводим ответ отправленного post запроса
    print('result_post=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # заполняем тело put запроса (url берем тот же)
    request_put = {}
    request_put['id'] = str(requests_post.json()['id'])
    request_put['name'] = 'Sberdog'
    request_put['photoUrls'] = ['Photodog']
    # выведем тело сформированного post запроса для проверки
    print('request_put=', request_put)
    # отправим put запрос
    request_put_r = requests.put(url, json=request_put, verify=False)
    # выводим ответ отправленного put запроса
    print('result_put=', json.dumps(request_put_r.json(), indent=4, sort_keys=True))

def test_del_pet():
    # сформируем и отправим post запрос для создания сущности на удаление
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = 'sbercat'
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'

    requests_post = requests.post(url, json=request, verify=False)
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # сформируем url для delete запроса, id возьмем с предыдущего post запроса
    url_del = "https://petstore.swagger.io/v2/pet/" + str(requests_post.json()['id'])
    # выполняем delete запрос и выводим результат запроса
    request_del = requests.delete(url_del, verify=False)
    print("result_del=", json.dumps(request_del.json(), indent=4, sort_keys=True))

def test_put_pet_assert():
    # задаем url и заполняем тело запроса
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = 'sbercat'
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем post запрос
    requests_post = requests.post(url, json=request, verify=False)
    # проверяем результат запроса
    print('result_post=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # создаем новое наполнение в тело запроса
    request_put = {}
    #  id берем с ответа на предыдущий запрос
    request_put['id'] = str(requests_post.json()['id'])
    request_put['name'] = 'Sberdog'
    request_put['photoUrls'] = ['Photodog']
    #  проверяем что получилось в теле запроса
    print('request_put=', request_put)
    #  отправляем put запрос
    request_put_r = requests.put(url, json=request_put, verify=False)
    #  проверяем ответ на запрос
    print('result_put=', json.dumps(request_put_r.json(), indent=4, sort_keys=True))
    # указываем url для get запроса, id берем с ответа на первый запрос
    url_get = "https://petstore.swagger.io/v2/pet/" + str(requests_post.json()['id'])
    # проверяем что данные изменились
    request_get = requests.get(url_get, verify=False)
    # проверяем что параметр name get запроса совпадает с параметром name put запроса
    assert request_get.json()['name'] == request_put['name']

def test_put_pet_negative():
    # задаем url и заполняем тело запроса
    url = "https://petstore.swagger.io/v2/pet"

    request_put = {}
    request_put['id'] = []
    request_put['name'] = 'Sberdog'
    request_put['photoUrls'] = ['Photodog']
    # отправляем put запрос
    request_put_r = requests.put(url, json=request_put, verify=False)
    # проверяем ответ на запрос
    print('result_put=', json.dumps(request_put_r.json(), indent=4, sort_keys=True))
    # проверяем поле message
    assert request_put_r.json()['message'] == "something bad happened"


def test_delete_pet_negative():
    # сформируем и отправим post запрос для создания сущности
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = 'sbercat'
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'

    requests_post = requests.post(url, json=request, verify=False)
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # проверяем ответ
    assert str(requests_post).__contains__('200')
    # задаем url с не корректным id
    url_del = "https://petstore.swagger.io/v2/pet/" + 'sda'
    # отправляем запрос
    request_del = requests.delete(url_del, verify=False)
    # выводим результат запроса
    print("result_del=", json.dumps(request_del.json(), indent=4, sort_keys=True))
    # проверяем ответ
    assert str(request_del).__contains__('404')


def test_post_image():
    # сформируем и отправим post запрос для создания сущности
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = 'sberDog'
    request['photoUrls'] = ['photoDog']
    request['category'] = {}
    request['category']['name'] = 'dogs'

    requests_post = requests.post(url, json=request, verify=False)
    print('result_post=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # сформируем post запрос для отправки аттача с id ответа на прошлый запрос
    url_image = "https://petstore.swagger.io/v2/pet/" + str(requests_post.json()['id']) + "/uploadImage"
    # откроем файл для чтения
    file = for_files.open_file('venv/Scripts/files/send.txt')
    # отправляем post запрос с аттачем
    post_file = requests.post(url_image, files=file, verify=False)
    # выводим url на который отправили запрос для проверки сформированного id, и проверяем ответ на запрос
    print('response = ', url_image, post_file)
    # закрываем файл
    for_files.close_file(file)
    # Проверка ответа на загрузку post запроса с аттачем
    assert post_file.json()['code'] is not None

def test_post_image_negative():
    # сформируем и отправим post запрос для создания сущности
    url = "https://petstore.swagger.io/v2/pet"
    request = {}
    request['name'] = 'sberDog'
    request['photoUrls'] = ['photoDog']
    request['category'] = {}
    request['category']['name'] = 'dogs'

    requests_post = requests.post(url, json=request, verify=False)
    print('result_post=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # сформируем post запрос для отправки без аттача с id ответа на прошлый запрос
    url_image = "https://petstore.swagger.io/v2/pet/" + str(requests_post.json()['id']) + "/uploadImage"
    # отправляем запрос
    post_file = requests.post(url_image, verify=False)
    # выводим url для проверки id и ответ который пришел
    print('response = ', url_image, post_file)
    # Проверка ответа на загрузку post запроса с аттачем
    assert str(post_file).__contains__("415")

def test_post_pet_update():
    # задаем url и наполняем тело запроса
    url = "https://petstore.swagger.io/v2/pet/"
    request = {}
    request['name'] = 'sbercat'
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем post запрос
    requests_post = requests.post(url, json=request, verify=False)
    # выводим ответ в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выполняем проверку что id в теле ответа не пустой
    assert requests_post.json()['id'] is not None
    # задаем url запроса, берем id из ответа предыдущего шага
    url_post = "https://petstore.swagger.io/v2/pet/" + str(requests_post.json()['id'])
    # наполняем тело запроса
    name = 'Ddog'
    status = 'Open'
    form_data = 'name=' + name + '&' + 'status=' + status
    # отправляем запрос
    request_update_post = requests.post(url_post, data=form_data, verify=False)
    # Выводим ответ на запрос
    print('update=', json.dumps(request_update_post.json(), indent=4, sort_keys=True))
    # проверка на ошибку
    assert str(request_update_post).__contains__('200')
    # для проверки изменений отправим get запрос с id указаным в ответе первого запроса
    url_get = url + str(requests_post.json()['id'])
    request_get = requests.get(url_get, verify=False)
    # выводим результа get запроса
    print('get request = ', json.dumps(request_get.json(), indent=4, sort_keys=True))
    # проверим что тело ответа на get запрос совпадает с телом отправленным в post запросе на изменения
    assert str(request_get).__contains__('200')
    assert request_get.json()['name'] == name
    assert request_get.json()['status'] == status

def test_post_pet_update_negative():
    # задаем url и наполняем тело запроса
    url = "https://petstore.swagger.io/v2/pet/"
    request = {}
    request['name'] = 'sbercat'
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    # отправляем post запрос
    requests_post = requests.post(url, json=request, verify=False)
    # выводим ответ в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    # выполняем проверку что id в теле ответа не пустой
    assert requests_post.json()['id'] is not None
    # задаем url запроса, указываем не существующий id
    url_post = "https://petstore.swagger.io/v2/pet/" + '77777777777778'
    # наполняем тело запроса
    name = 'Ddog'
    status = 'Open'
    form_data = 'name=' + name + '&' + 'status=' + status
    # отправляем запрос
    request_update_post = requests.post(url_post, data=form_data, verify=False)
    # Выводим ответ на запрос
    print('update=', json.dumps(request_update_post.json(), indent=4, sort_keys=True))
    # проверка на ошибку
    assert str(request_update_post).__contains__('404')
    assert request_update_post.json()['message'] == "not found"

def test_find_by_status():
    # задаем url
    url = "https://petstore.swagger.io/v2/pet/"
    # задаем тело запроса
    request = {}
    request['name'] = 'catcatcat'
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    request['status'] = 'available'
    # отправляем post запрос
    requests_post = requests.post(url, json=request, verify=False)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    url_get = "https://petstore.swagger.io/v2/pet/" + 'findByStatus?status=available'
    # отправляем get запрос
    request_get = requests.get(url_get, verify=False)
    # выводим ответ в формате json
    print('result get=', json.dumps(request_get.json(), indent=4, sort_keys=True))
    #выполняем проверку на статус код и что массив не пуст
    assert str(request_get).__contains__('200')
    assert request_get.json() != []

def test_find_by_status_negative():
    # задаем url
    url = "https://petstore.swagger.io/v2/pet/"
    # задаем тело запроса
    request = {}
    request['name'] = 'catcatcat'
    request['photoUrls'] = ['photocat']
    request['category'] = {}
    request['category']['name'] = 'cats'
    request['status'] = 'available'
    # отправляем post запрос
    requests_post = requests.post(url, json=request, verify=False)
    # выводим ответ на запрос в формате json
    print('result=', json.dumps(requests_post.json(), indent=4, sort_keys=True))
    url_get = "https://petstore.swagger.io/v2/pet/" + 'findByStatus?status=open'
    # выводим ответ в формате json
    request_get = requests.get(url_get, verify=False)
    print('result get=', json.dumps(request_get.json(), indent=4, sort_keys=True))
    # выполняем проверку на статус код и что массив пуст
    assert request_get.json() == []

