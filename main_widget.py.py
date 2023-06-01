from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup

class MainWidget(QWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super(MainWidget, self).__inint__(parent)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        