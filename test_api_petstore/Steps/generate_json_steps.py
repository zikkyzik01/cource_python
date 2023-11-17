from Steps import support_steps as support_steps
import  allure

# Создание JSON для метода post /pet с обязательными параметрами
def create_json_post_pet_required_params(id):
    with allure.step("Создание JSON для метода post /pet с обязательными параметрами"):
        request = {}
        request['id'] = id
        request['name'] = support_steps.generate_random_letter_string(6)
        request['photoUrls'] = [support_steps.generate_random_letter_string(8)]
        print("request = ", request)
        return request

# Создание JSON для метода post /pet с определенными параметрами
def create_json_post_pet_all_params(id, status):
    with allure.step("Создание JSON для метода post /pet с определенными параметрами"):
        request = {}
        request['id'] = id
        request['name'] = support_steps.generate_random_letter_string(6)
        request['photoUrls'] = [support_steps.generate_random_letter_string(8)]
        request['category'] = {}
        request['category']['name'] = support_steps.generate_random_letter_string(7)
        request['status'] = status
        request['tags'] = [{}]
        request['tags'][0]['name'] = support_steps.generate_random_letter_string(6)
        print("request = ", request)
        return request

# Создание JSON для метода post /user с определенными параметрами
def create_json_post_user_all_params(id, userstatus):
    with allure.step("Создание JSON для метода post /user с определенными параметрами"):
        request = {}
        request["id"] = id
        request["username"] = support_steps.generate_random_letter_string(5)
        request["firstName"] = support_steps.generate_random_letter_string(6)
        request["lastName"] = support_steps.generate_random_letter_string(7)
        request["email"] = support_steps.generate_random_letter_string_mail(8)
        request["password"] = support_steps.generate_random_letter_string(5)
        request["phone"] = support_steps.generate_random_number_string(11)
        request["userStatus"] = userstatus
        print("request = ", request)
        return request

# Создание пустого JSON для метода post /user
def create_json_post_user_not_params():
    with allure.step("Создание пустого JSON для метода post /user"):
        request = {}
        print("request = ", request)
        return request