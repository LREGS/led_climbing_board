from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)

class UI(QWidget):
    def __init__(self):
        super().__init__()
        
        uic.loadUi('boardgui.ui', self)
        


window = UI()
window.show()
sys.exit(app.exec())