
# Функция проверяет что id не пустой
def assert_not_none_id(request):
    assert request.json()['id'] is not None

# Функция проверяет что id запросов равны
def assert_equals_response_ids(first, second):
    assert first.json()['id'] == second.json()['id']

# Функция проверяет что message ответа равен заданному
def assert_not_correct_message(request, message):
    assert request.json()['message'] == message

# Функция проверяет что name ответа и запроса равны
def assert_equals_response_params(first, second):
    assert str(first.json()['name']) == second['name']

# Функция проверяет что статус код равен заданному
def assert_status_code(request, status_code):
    assert str(request).__contains__(status_code)

# Функция проверяет что name ответа и запроса равны
def assert_equals_response_params_name(first, second):
    assert str(first.json()['name']) == str(second.json()['name'])

# Функция проверяет что параметр не пустой
def assert_is_not_none(request, params):
    assert request.json()[params] is not None

# Функция проверяет что полученное значение совпадает с параметром
def assert_equals_params(request, outparams, inparams):
    assert request.json()[outparams] == inparams

# Функция проверяет что полученный массив пуст
def assert_massive_null(response):
    assert response.json() == []

# Функция проверяет что полученный массив не пуст
def assert_massive(response):
    assert response.json() != []

# Функция проверяет что name ответа и запроса равны
def assert_equals_response_params_username(first, second):
    assert first.json()['username'] == second["username"]