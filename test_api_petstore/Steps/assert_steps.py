
# Функция проверяет что id не пустой
def assert_not_none_id(request):
    assert request.json()['id'] is not None

# Функция проверяет что id запросов равны
def assert_equals_response_ids(first, second):
    assert first.json()['id'] == second.json()['id']

# Функция проверяет что message ответа не корректный
def assert_not_correct_message(request):
    assert request.json()['message'] == "something bad happened"

# Функция проверяет что статус код равен 404
def assert_not_found(request):
    assert str(request).__contains__('404')

# Функция проверяет что name ответа и запроса равны
def assert_equals_response_params(first, second):
    assert str(first.json()['name']) == second['name']

# Функция проверяет что статус код равен 200
def assert_correct_code(request):
    assert str(request).__contains__('200')

# Функция проверяет что name ответа и запроса равны
def assert_equals_response_params_name(first, second):
    assert str(first.json()['name']) == str(second.json()['name'])

# Функция проверяет что параметр не пустой
def assert_is_not_none(request, params):
    assert request.json()[params] is not None

# Функция проверяет что статус код равен 415
def assert_negative(response):
    assert str(response).__contains__("415")

# Функция проверяет что полученное значение совпадает с параметром
def assert_equals_params(request, outparams, inparams):
    assert request.json()[outparams] == inparams

# Функция проверяет что полученный массив пуст
def assert_massive_null(response):
    assert response.json() == []

# Функция проверяет что полученный массив не пуст
def assert_massive(response):
    assert response.json() != []

# Функция проверяет что статус код равен 500
def assert_negative_500(response):
    assert str(response).__contains__('500')

# Функция проверяет что user не найден
def assert_user_not_found(request):
    assert str(request).__contains__('404')
    assert request.json()['message'] == "User not found"

# Функция проверяет что name ответа и запроса равны
def assert_equals_response_params_username(first, second):
    assert first.json()['username'] == second["username"]