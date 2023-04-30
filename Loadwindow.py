from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt6 import uic
import sys

app = QApplication(sys.argv)

class UI(QWidget):
    def __init__(self):
        super().__init__()
        
        uic.loadUi('boardgui.ui', self)
        


window = UI()
window.show()
sys.exit(app.exec())