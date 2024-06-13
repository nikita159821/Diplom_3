import random
import string

import allure


@allure.step('Генерация случайных данных для пользователя')
def generate_user_data():
    email = f"test-data-{random.randint(1, 10000)}@yandex.ru"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    name = f"TestUser{random.randint(1, 100)}"
    return email, password, name