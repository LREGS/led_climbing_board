import PySide6.QtCore
from PySide6.QtWidgets import QButtonGroup, QPushButton 

class HoldButtonGroup():
    
    def __init__(self, boardWidget):
        super().__init__()
        self.boardWidget = boardWidget
        self.button_group = QButtonGroup()
        
        def create_group(boardWidget):
            for i in range(1, 28):
                hold = boardWidget.findChild(QPushButton, f''hold{i})
                self.button_group.addButton(hold, i)
        