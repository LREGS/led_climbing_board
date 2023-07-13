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
        self.grade = []
        
        
    def populate_table(self):
        with open\
        ('/home/william/Desktop/climbing_board/data/climbs_dict.json', 'r') as f: 
            my_dict = json.load(f)
            
        self.names = [name for name in my_dict.keys()]
        self.widget.tableWidget.setRowCount(len(self.names))
        
        for row, name in enumerate(self.names):
            row_name = QTableWidgetItem(str(name))
            self.widget.tableWidget.setItem(row, 0, row_name)
            
            row_grade = QTableWidgetItem(str(my_dict[name]['grade']))
            self.widget.tableWidget.setItem(row, 1, row_grade)      
            
        print(self.grade)
        print('table completd')
