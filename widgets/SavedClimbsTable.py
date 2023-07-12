import os
import json

from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem

from ui_py_files.saved_climbs_table_ui import Ui_Form

class SavedClimbsTable(QWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super(SavedClimbsTable, self).__init__(parent)
        self.widget = Ui_Form()
        self.setLayout(QVBoxLayout())
        self.widget.setupUi(self)
        
    def populate_table(self):
        with open\
        ('/home/william/Desktop/climbing_board/data/climbs_dict.json', 'r') as f: 
            my_dict = json.load(f)
            
            for row, item in enumerate(my_dict):
    # Add the value of the first key to the first column
                first_key = list(item.keys())[0]
                self.widget.setItem(row, 0, QTableWidgetItem(str(item[first_key])))

    # Add the value of the second key to the second column
                self.widget.setItem(row, 1, QTableWidgetItem(str(item['second_key'])))