import os

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup

from BoardWidget import BoardWidget

class MainWidget(QWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super(MainWidget, self).__init__(parent)
        #add board widdget
        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)

        self.board_widget = BoardWidget()
        
        self.main_layout.addWidget(self.board_widget)