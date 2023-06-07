import os 

from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QButtonGroup

#from BoardWidgetUi import UiBoardWidget
from boardgui import Ui_board_widget

"""Add methods to manipulate ui and connect signals to slots"""

class BoardWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None) -> None:
        super(BoardWidget, self).__init__(parent)
        self.widget = Ui_board_widget()
        self.setLayout(QVBoxLayout())
        self.widget.setupUi(self)
        self.route = []
#This value doesn't seem to be getting updated when the creat_climb button is p
# self.creating_climb = False
        self.hold_buttons = self.create_button_group()

        #self.hold_buttons.buttonClicked.connect(self.collect_route)
        
    def create_button_group(self):
        button_group = QButtonGroup()
        for i in range(1,28):
            button_name = f'hold{i}'
            button = getattr(self.widget, button_name, None)
            if button:
                button_group.addButton(button, i)
        print(button_group)
        return button_group

    
    def handle_create_climb_clicked(self):
        print('click on the holds you want to include in the route')
        
    # def collect_route(self, button):
    #     # if self.creating_climb == False:
    #     #     print("you haven't started creating a climb yet")
    #     # elif self.creating_climb == True:
    #         hold_selected = self.hold_buttons.id(button)
    #         self.route.append(hold_selected)
    #         print(self.route)
    