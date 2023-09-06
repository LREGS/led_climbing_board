import os

from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem

from ui_py_files.saved_climbs_table_ui import Ui_Form
from configuration_copy import Climbs

class SavedClimbsTable(QWidget):
    def __init__(self, db: Climbs = None, parent: QWidget = None) -> None:
        super(SavedClimbsTable, self).__init__(parent)
        self.widget = Ui_Form()
        self.setLayout(QVBoxLayout())
        self.widget.setupUi(self)

        self.setFixedSize(400,400)

        self.db = db

        self.table = self.widget.tableWidget

        self.populate_table()
        
    def populate_table(self):

        self.db.cursor.execute("SELECT climb_name, route, grade from climbs")
        data = self.db.cursor.fetchall()

        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.table.setItem(i, j, item)



        # self.names = [name for name in saved_climbs_data.keys()]
        # self.widget.tableWidget.setRowCount(len(self.names))

        # for row, name in enumerate(self.names):
        #     row_name = QTableWidgetItem(str(name))
        #     self.widget.tableWidget.setItem(row, 0, row_name)
            
        #     row_grade = QTableWidgetItem(str(saved_climbs_data[name]['grade']))
        #     self.widget.tableWidget.setItem(row, 1, row_grade)  

        #     # row_ticks = QTableWidgetItem(str(saved_climbs_data[name]['ticks']))
        #     # self.widget.tableWidget.setItem(row, 2, row_ticks)

            """guess ticks will need to be added in by querying the other database """


                    
