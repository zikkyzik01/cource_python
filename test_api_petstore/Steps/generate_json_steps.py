from Steps import support_steps as support_steps

# Создание JSON для метода post /pet с обязательными параметрами
def create_json_post_pet_required_params(id):
    request = {}
    request['id'] = id
    request['name'] = support_steps.generate_random_letter_string(6)
    request['photoUrls'] = [support_steps.generate_random_letter_string(8)]
    print("request = ", request)
    return request

# Создание JSON для метода post /pet с обязательными параметрами
def create_json_post_pet_all_params(id, status):
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

def create_json_post_user_all_params(id, userstatus):
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

def create_json_post_user_not_params():
    request = {}
    print("request = ", request)
    return request

def create_json_post_user_update_params(param):
    request = {}
    request["id"] = param
    request["username"] = support_steps.generate_random_letter_string(5)
    request["firstName"] = support_steps.generate_random_letter_string(6)
    request["lastName"] = support_steps.generate_random_letter_string(7)
    request["email"] = support_steps.generate_random_letter_string_mail(8)
    request["password"] = support_steps.generate_random_letter_string(5)
    request["phone"] = support_steps.generate_random_number_string(11)
    request["userStatus"] = support_steps.generate_random_number_string(5)
    print("request = ", request)
    return request