from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup

class MainWidget(QtWidgets.Widget):
    super(MainWidget, self).__init__(parent)
    self.main_layout = QVBoxLayout()
    