from PySide6.QtWidgets import QButtonGroup, QPushButton
from main import boart_widget

def hold_buttons_f(self):
    self.hold_buttons = QButtonGroup()
    for i in range(1, 28):
        hold = board_wedget.findChild(QPushButton, f'hold{i}')
        self.hold_buttons.addButton(hold, i)