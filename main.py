from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
import sys
import webbrowser

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 250)
        self.setWindowTitle("GeNERation DaTa")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = QLineEdit()
        self.input.setFixedWidth(150)
        layout.addWidget(self.input, alignment= Qt.AlignmentFlag.AlignCenter)

        button = QPushButton("Generate")
        button.clicked.connect(self.get)
        layout.addWidget(button)


    def get(self):
        text = self.input.text()
        webbrowser.open_new(text)

    
        

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())

