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
        self.route = []

        self.widget.hold_buttons.buttonClicked.connect(self.collect_route)
    
    def handle_create_climb_clicked(self):
        print('creating cimb')
        
    def collect_route(self):
        # hold_selected = self.widget.hold_buttons.id(button)
        # self.route.append(hold_selected)
        # print(self.route)
        print('hi)')
