import allure

# Функция проверяет что id не пустой
def assert_not_none_id(request):
    with allure.step("Функция проверяет что id не пустой"):
        assert request.json()['id'] is not None

# Функция проверяет что id запросов равны
def assert_equals_response_ids(first, second):
    with allure.step("Функция проверяет что id запросов равны"):
        assert first.json()['id'] == second.json()['id']

# Функция проверяет что message ответа равен заданному
def assert_not_correct_message(request, message):
    with allure.step("Функция проверяет что message ответа равен заданному"):
        assert request.json()['message'] == message

# Функция проверяет что name ответа и запроса равны
def assert_equals_response_params(first, second):
    with allure.step("Функция проверяет что name ответа и запроса равны"):
        assert str(first.json()['name']) == second['name']

# Функция проверяет что статус код равен заданному
def assert_status_code(request, status_code):
    with allure.step("Функция проверяет что статус код равен заданному"):
        assert str(request).__contains__(status_code)

# Функция проверяет что name ответа и запроса равны
def assert_equals_response_params_name(first, second):
    with allure.step("Функция проверяет что name ответа и запроса равны"):
        assert str(first.json()['name']) == str(second.json()['name'])

# Функция проверяет что параметр не пустой
def assert_is_not_none(request, params):
    with allure.step("Функция проверяет что параметр не пустой"):
        assert request.json()[params] is not None

# Функция проверяет что полученное значение совпадает с параметром
def assert_equals_params(request, outparams, inparams):
    with allure.step("Функция проверяет что полученное значение совпадает с параметром"):
        assert request.json()[outparams] == inparams

# Функция проверяет что полученный массив пуст
def assert_massive_null(response):
    with allure.step("Функция проверяет что полученный массив пуст"):
        assert response.json() == []

# Функция проверяет что полученный массив не пуст
def assert_massive(response):
    with allure.step("Функция проверяет что полученный массив не пуст"):
        assert response.json() != []

# Функция проверяет что name ответа и запроса равны
def assert_equals_response_params_username(first, second):
    with allure.step("Функция проверяет что name ответа и запроса равны"):
        assert first.json()['username'] == second["username"]