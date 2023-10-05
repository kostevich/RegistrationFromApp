from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
from selenium.webdriver.common.by import By
from selenium import webdriver 
from Sourсe.RandomUserData import *
from time import sleep 

import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 250)
        self.setWindowTitle("GeNERation DaTa")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = QLineEdit()
        self.input.setFixedWidth(250)
        layout.addWidget(self.input, alignment= Qt.AlignmentFlag.AlignCenter)

        button = QPushButton("Generate")
        button.clicked.connect(self.EnterUser)
        layout.addWidget(button)

    # Ввод данных пользователя на сайте.
    def EnterUser(self):
        # Открытие браузера.
        driver = webdriver.Edge()
        # Открытие ссылки.
        driver.get(self.input.text())
        # Cоздание данных пользователя.
        User = GenerateUser()
        # Ввод данных пользователя в нужные поля.
        driver.find_element(By.NAME,"Name").send_keys(GenerateUser.username) 
        driver.find_element(By.NAME,"Email").send_keys(GenerateUser.email) 
        driver.find_element(By.NAME,"tildaspec-phone-part[]").send_keys(GenerateUser.number)
        # Нажатие кнопки. 
        driver.find_element(By.CLASS_NAME, "t-submit").click()
        sleep(10) 
    

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())

