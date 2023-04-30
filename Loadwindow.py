from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
import sys

class UI(QWidget):
    def __init__(self):
        super().__init__()
        
        uic.load_ui('boardgui.ui', self)

app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())