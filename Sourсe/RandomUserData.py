from faker import Faker

import random

# Генерация рандомных данных пользователя.
def GenerateUser():
    # Создание экземпляра класса.
    fake = Faker()
    # Генерация имени и фамилии.
    username = fake.name()
    # Генерация email.
    email = ''.join(username.split()).lower() + random.choice(['@gmail.com', '@mail.com','@outlook.com', '@aol.com', '@yahoo.com', '@hotmail.com', '@mail.ru', '@ya.ru', '@yandex.ru'])
    # Генерация номера телефона.
    number = '+375' + random.choice(['24', '25', '29', '33', '44']) + str(random.randint(1000000,9999999))
    # Возвращает данные пользователя.
    return username, email, number

