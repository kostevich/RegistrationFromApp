from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
import sys
from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep 
from Sourse.RandomUserData import *



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


    

    def EnterUser(self):
        driver = webdriver.Edge()
        driver.get(self.input.text())
        User = GenerateUser(self)
        driver.find_element(By.NAME,"Name").send_keys(self.username) 
        driver.find_element(By.NAME,"Email").send_keys(self.email) 
        driver.find_element(By.NAME,"tildaspec-phone-part[]").send_keys(self.number) 
        driver.find_element(By.CLASS_NAME, "t-submit").click()
        sleep(10) 
    

        

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())

