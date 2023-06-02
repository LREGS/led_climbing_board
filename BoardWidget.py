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
        self.creating_climb = False

        self.widget.hold_buttons.buttonClicked.connect(self.collect_route)
    
    def handle_create_climb_clicked(self):
        print('click on the holds you want to include in the route')
        
    def collect_route(self, button):
        if self.creating_climb == False:
            print("you haven't started creating a climb yet")
        elif self.creating_climb == True:
            hold_selected = self.widget.hold_buttons.id(button)
            self.route.append(hold_selected)
            print(self.route)