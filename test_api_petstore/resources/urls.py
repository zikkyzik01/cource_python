main_url = "https://petstore.swagger.io/v2/"

url_pet = main_url + "pet"
url_user = main_url + "user"

def url_pet_get(pet_info):
    return main_url + "pet/" + pet_info

def url_user_get(user_info):
    return main_url + "user/" + user_info