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

    
    #this is running through the whole db everytime something new is added and cannot
    # be the best way to keep it updated ! Itll get so slow     
    def populate_table(self):

        self.db.cursor.execute("SELECT climb_name, grade from climbs")
        data = self.db.cursor.fetchall()

        self.table.setRowCount(len(data))

        #this doesn't work if there's no data in the column already         
        self.table.setColumnCount(len(data[0]))


        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.table.setItem(i, j, item)





                    
