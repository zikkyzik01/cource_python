import random
import string
import allure

# Функция генерирует строку чисел 0-9 заданной длины
def generate_random_number_string(length):
    with allure.step("Функция генерирует строку чисел 0-9 заданной длины"):
        result = ""
        for i in range(0, length):
            result += str(random.randint(0, 9))
        return result

# Функция генерирует строку заданной длины
def generate_random_letter_string(length):
    with allure.step("Функция генерирует строку чисел 0-9 заданной длины"):
        result = ""
        for i in range(0, length):
            result += str(random.choice(string.ascii_letters[random.randint(0, 5)]))
        return result

# Функция генерирует строку заданной длины для параметра email
def generate_random_letter_string_mail(length):
    with allure.step("Функция генерирует строку заданной длины для параметра email"):
        result = ""
        for i in range(0, length):
            result += str(random.choice(string.ascii_letters[random.randint(0, 5)]))
        return result + '@mail.net'

