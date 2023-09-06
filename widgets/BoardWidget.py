import os 

from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QButtonGroup

from ui_py_files.boardgui_2 import Ui_board_widget

class BoardWidget(QtWidgets.QWidget):
    '''Controls and represents the climbing board and the buttons that represent the holds'''
    def __init__(self, parent: QtWidgets.QWidget = None) -> None:
        super(BoardWidget, self).__init__(parent)
        self.widget = Ui_board_widget()
        self.setLayout(QVBoxLayout())
        self.widget.setupUi(self)

        self.setFixedSize(400,400)
        
        self.hold_buttons_group = self.create_button_group()
        self.hold_buttons_group.setExclusive(False)
        
        self.hold_buttons = self.hold_buttons_group.buttons()

    #creates the holds buttons users use to create climbs
    def create_button_group(self):
        button_group = QButtonGroup()
        #magic number needs removing
        for i in range(1,60):
            button_name = f'hold{i}'
            button = getattr(self.widget, button_name, None)
            if button:
                button.setEnabled(False)
                button_group.addButton(button, i)
        print(button_group)
        return button_group

    #can these be refactored into one?        
    def enable_buttons(self):
        for button in self.hold_buttons_group.buttons():
            button.setEnabled(True)

    def disable_buttons(self):
        for button in self.hold_buttons_group.buttons():
            button.setEnabled(False)
    
    def uncheck_buttons(self):
        for button in self.hold_buttons_group.buttons():
            button.setChecked(False)



    

