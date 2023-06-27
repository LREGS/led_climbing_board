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
        
        self.hold_buttons_group = self.create_button_group()
        self.hold_buttons = self.hold_buttons_group.buttons()

        self.toggle_tracker = False

        
    def create_button_group(self):
        button_group = QButtonGroup()
        for i in range(1,28):
            button_name = f'hold{i}'
            button = getattr(self.widget, button_name, None)
            if button:
                button_group.addButton(button, i)
        print(button_group)
        return button_group

    
    def toggle_hold_buttons(self, arg):
        for button in self.hold_buttons:
            button.setEnabled(arg)
    
    def button_colour_active(self, id):
        hold_name = f'hold{id}'
        hold_value = getattr(self.widget, hold_name)
        if self.toggle_tracker == False:
            hold_value.setStyleSheet("background-color: green;")
            self.toggle_tracker = True
        elif self.toggle_tracker == True:
            hold_value.setStyleSheet("background-color: red;")
            self.toggle_tracker = False
    

    
    def button_colour_reset(self):
        return
        
