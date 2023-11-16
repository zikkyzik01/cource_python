import requests

# Отправка запроса и получение ответа для метода POST
# url - эндпоинт
# request - JSON
def request_post(url, request):
    request = requests.post(url, json=request, verify=False)
    return request

# Отправка запроса и получение ответа для метода GET
# url - эндпоинт
def request_get(url):
    request = requests.get(url, verify=False)
    return request

def request_put(url, request):
    request = requests.put(url, json=request, verify=False)
    return request

def request_delete(url):
    request = requests.delete(url, verify=False)
    return request

def request_file(url, file):
    request = requests.post(url, files=file, verify=False)
    return request

def request_data(url, data):
    request = requests.post(url, data=data, verify=False)
    return request
