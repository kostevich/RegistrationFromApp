
import random

from faker import Faker

fake = Faker()



def GenerateUser(self):
    self.username = fake.name()
    self.email = ''.join(self.username.split()).lower() + random.choice(['@gmail.com', '@mail.com','@outlook.com', '@aol.com', '@yahoo.com', '@hotmail.com', '@mail.ru', '@ya.ru', '@yandex.ru'])
    self.number = '+375' + random.choice(['24', '25', '29', '33', '44']) + str(random.randint(1000000,9999999))

    return self.username, self.email, self.number

