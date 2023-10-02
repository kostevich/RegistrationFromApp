
import random

from faker import Faker

fake = Faker()



def GenerateNameMail():
    
    username = fake.name()
    
    email = ''.join(username.split()).lower() + random.choice(['@gmail.com', '@mail.com','@outlook.com', '@aol.com', '@yahoo.com', '@hotmail.com', '@mail.ru', '@ya.ru', '@yandex.ru'])
    
    print(username, email)




def GeneratePhoneNumber():

    number = '+375' + random.choice(['24', '25', '29', '33', '44']) + str(random.randint(1000000,9999999))

    print(number)



GenerateNameMail()

GeneratePhoneNumber()
