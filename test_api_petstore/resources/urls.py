main_url = "https://petstore.swagger.io/v2/"

url_pet = main_url + "pet/"
url_user = main_url + "user/"

def url_pet_get(pet_id):
    return main_url + "pet/" + pet_id

def url_user_get(user_id):
    return main_url + "user/" + user_id

def url_pet_find_by_status(status):
    return url_pet + "findByStatus?status=" + status

def url_pet_upload(pet_id):
    return url_pet + pet_id + "/uploadImage"