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

        for row, name in enumerate(self.names):
            row_name = QTableWidgetItem(str(name))
            self.widget.tableWidget.setItem(row, 0, row_name)
            
            row_grade = QTableWidgetItem(str(saved_climbs_data[name]['grade']))
            self.widget.tableWidget.setItem(row, 1, row_grade)  

            row_ticks = QTableWidgetItem(str(saved_climbs_data[name]['ticks']))
            self.widget.tableWidget.setItem(row, 2, row_ticks)


                    
