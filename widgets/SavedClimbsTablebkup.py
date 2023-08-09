import os

from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem

from ui_py_files.saved_climbs_table_ui import Ui_Form
from tools.JsonHandler import JsonHanlder as Json

class SavedClimbsTable(QWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super(SavedClimbsTable, self).__init__(parent)
        self.widget = Ui_Form()
        self.setLayout(QVBoxLayout())
        self.widget.setupUi(self)

        self.setFixedSize(400,400)

        self.grade = []

        self.climbsJSON = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'climbs_dict.json')
        
        
    def populate_table(self):

        saved_climbs_data = Json.openJson(self.climbsJSON)
        self.names = [name for name in saved_climbs_data.keys()]
        self.widget.tableWidget.setRowCount(len(self.names))

        main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   
        relative_path = 'data/climbs_dict.json'
        data_file_path = os.path.join(main_folder, relative_path)

        with open\
        (data_file_path, 'r') as f: 
            my_dict = json.load(f)
            
        self.names = [name for name in my_dict.keys()]
        self.widget.tableWidget.setRowCount(len(self.names))
        
        for row, name in enumerate(self.names):
            row_name = QTableWidgetItem(str(name))
            self.widget.tableWidget.setItem(row, 0, row_name)
            
            row_grade = QTableWidgetItem(str(my_dict[name]['grade']))
            self.widget.tableWidget.setItem(row, 1, row_grade)  
            
            print(my_dict[name]['route'])    
            
        print(self.grade)
        print('table completd')
