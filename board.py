#board.py

from PySide6.QtWidgets import QPushButton, QButtonGroup

class BoardWidget:
    def __init__(self, widget):
        self.widget = widget 
        self.hold_buttons = QButtonGroup()
        for i in range (1, 28):
            hold = self.widget.findChild(QPushButton, f'hold{i}')
            self.hold_buttons.addButton(hold, i)
        return
    
    def get_hold_id(self, button):
        return self.hold_buttons.id(button)