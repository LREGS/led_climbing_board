import os 

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QVBoxLayout

from BoardWidgetUi import UiBoardWidget

"""Add methods to manipulate ui and connect signals to slots"""

class BoardWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None) -> None:
        super(BoardWidget, self).__init__(parent)
        self.widget = UiBoardWidget()
        self.setLayout(QVBoxLayout())
        self.widget.setupUi(self)

        
    def board_function(self):
        return 
    def board_function2(self):
        return
        
