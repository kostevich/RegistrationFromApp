# RegistrationFromApp 
**RegistrationFromApp** – приложение на [pqt6](https://github.com/piotrkowalczuk/pqt?ysclid=lq2khsyn8x955167959), которое вводит случайное, корректное имя пользователя, email, и номер телефона.

# Порядок установки и использования
1. Загрузить репозиторий. Распаковать.
2. Установить [Python](https://www.python.org/downloads/) версии не старше 3.11. Рекомендуется добавить в PATH.
3. В среду исполнения установить следующие пакеты: [dublib](https://github.com/DUB1401/dublib), [Faker](https://github.com/faker-js/faker?ysclid=lq2kldnkwh96315556), [pyinstaller](https://github.com/pyinstaller?ysclid=lq2kngqhkw347498835), [pqt6](https://github.com/piotrkowalczuk/pqt?ysclid=lq2khsyn8x955167959), [selenium](https://github.com/SeleniumHQ/selenium?ysclid=lq2kp84y1834877858).
```
pip install Faker
pip install git+https://github.com/DUB1401/dublib
pip install pyinstaller
pip install pyqt6
pip install selenium
```
Либо установить сразу все пакеты при помощи следующей команды, выполненной из директории скрипта.
```
pip install -r requirements.txt
```
3. Открыть dist\main.exe.
4. В поле ввода приложения вставить http://over.org.tilda.ws/testuser.

# Пример работы
**Автоматическое заполнение информации на сайте:**

![image](https://github.com/kostevich/RegistrationFromApp/assets/109979502/96bd3846-bdf4-4251-9e27-9622b04ff003)

_Copyright © Kostevich Irina. 2023._


