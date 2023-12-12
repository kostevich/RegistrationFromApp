 #!/usr/bin/python

#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QVBoxLayout, QWidget
from selenium import webdriver 
from selenium.webdriver.common.by import By
from Sourсe.RandomUserData import *
from time import sleep 


import sys

#==========================================================================================#
# >>>>> СОЗДАНИЕ ПРИЛОЖЕНИЯ <<<<< #
#==========================================================================================#

# Создадим приложение наследующее функции класса QWidget.
class Window(QWidget):
    # Конструктор приложения.
    def __init__(self):
        super().__init__()

        # Размер окна приложения.
        self.resize(400, 250)

        # Название приложения.
        self.setWindowTitle("GeNERation DaTa")

        # Фон приложения.
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Поле ввода текста.
        self.input = QLineEdit()

        # Размер поля.
        self.input.setFixedWidth(250)

        # Положение поля.
        layout.addWidget(self.input, alignment= Qt.AlignmentFlag.AlignCenter)

        # Создание кнопки.
        button = QPushButton("Generate")

        # Переход по ссылке при нажатии кнопки.
        button.clicked.connect(self.EnterUser)

        # Создание кнопки.
        layout.addWidget(button)

#==========================================================================================#
# >>>>> ВВОД ДАННЫХ НА САЙТЕ <<<<< #
#==========================================================================================#

    # Ввод данных пользователя на сайте.
    def EnterUser(self):
        # Открытие браузера.
        driver = webdriver.Edge()

        # Открытие ссылки.
        driver.get(self.input.text())

        # Пока не закрыли окошко браузера.
        while True:
            # Формирование данных пользователя.
            username, email, number =  GenerateUser()

            # Ввод данных пользователя в нужные поля.
            driver.find_element(By.NAME,"Name").send_keys(username) 
            driver.find_element(By.NAME,"Email").send_keys(email) 
            driver.find_element(By.NAME,"tildaspec-phone-part[]").send_keys(number)

            # Нажатие кнопки. 
            driver.find_element(By.CLASS_NAME, "t-submit").click()

            # Ожидание 20 секунд.
            sleep(20)

            # Обновление страницы.
            driver.refresh() 
        
#==========================================================================================#
# >>>>> ИНИЦИАЛИЗАЦИЯ СКРИПТА <<<<< #
#==========================================================================================#

# Создаем экземпляр класса.
app = QApplication(sys.argv)

# Иконка приложения.
app.setWindowIcon(QtGui.QIcon("auth.ico"))

# Создаем виджет.
window = Window()
# Открытие окна приложения.
window.show()

#==========================================================================================#
# >>>>> вЫХОД ИЗ ПРИЛОЖЕНИЯ <<<<< #
#==========================================================================================#

# Выход из приложения.
sys.exit(app.exec())

