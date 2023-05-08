#importing components
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import os, sys


def clicked_button(data):
    print('Why?', data)
    
app = QApplication()
button = QPushButton('Add Climb')
button.setCheckable(True)

button.clicked.connect(clicked_button)

button.show()
app.exec()


