import os

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup

from load_ui_file import ui_loader as UI_BoardWidget
from button_group import create_button_group

class MainWidget(QWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super(MainWidget, self).__inint__(parent)
        #add board widget

        self.hold_button_group = create_button_group(self.board_widget)