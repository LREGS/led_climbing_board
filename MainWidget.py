import os
import csv

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup, \
QTableWidget, QGridLayout, QTableWidgetItem
from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtGui import QPalette, QColor


from BoardWidget import BoardWidget
from create_climb_form_widget import CreateClimbForm
from create_climb_formUI import Ui_Form

class MainWidget(QWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super(MainWidget, self).__init__(parent)
        
        #print statements need adding to a dlg box within the ui and not
        #printing in console
        
        self.main_layout = QGridLayout(self)
        self.setLayout(self.main_layout)

        self.board_widget = BoardWidget()
        self.board_widget.hold_buttons_group.buttonClicked.connect\
        (self.collect_route)
        
        self.create_climb_form_widget = CreateClimbForm()
        self.create_climb_form_widget.widget.saveClimb.setEnabled(False)
        self.create_climb_form_widget.widget.cancelcreation.setEnabled(False)
        
        """Needs to be added into own module"""
        self.saved_climbs_table = QTableWidget()
        self.saved_climbs_table.setColumnCount(3)
        self.saved_climbs_table.setRowCount(3)
        self.saved_climbs_table.setFixedSize(200,200)
        self.csv_data = self.read_climbs_csv('climbs.csv')
        self.populate_table(self.saved_climbs_table, self.csv_data)
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.refresh_table)
        # self.timer.start(1000)
        self.saved_climbs_table.cellClicked.connect(self.load_climb)
        
        self.create_climb_form_widget.widget.saveClimb.clicked.connect\
        (self.save_climb_data)
        self.create_climb_form_widget.widget.cancelcreation.clicked.connect\
        (self.handle_cancel_create_climb)
        
        self.create_climb_btn = QPushButton('Create Climb')
        self.create_climb_btn.clicked.connect(self.handle_create_climb)
                
        self.main_layout.addWidget(self.board_widget, 0,0)
        self.main_layout.addWidget(self.create_climb_btn, 1,0)        
        self.main_layout.addWidget(self.create_climb_form_widget, 0,1)  
        self.main_layout.addWidget(self.saved_climbs_table, 0,2)

        self.route = []
        
    def handle_create_climb(self):
        self.create_climb_btn.setEnabled(False)
        self.create_climb_form_widget.widget.saveClimb.setEnabled(True)
        self.create_climb_form_widget.widget.cancelcreation.setEnabled(True)
        self.board_widget.toggle_hold_buttons(True)


    def collect_route(self, button):
        if self.create_climb_btn.isEnabled() == True:
            print('Please press create climb first')
        elif button.isChecked() == True:
            self.route.append(self.board_widget.hold_buttons_group.id(button))
            button.setStyleSheet("background-color: green;")
            print(self.route)
        else:
            self.route.remove(self.board_widget.hold_buttons_group.id(button))
            button.setStyleSheet("background-color: transparent;")
            print(self.route)
        

    def save_climb_data(self):
        self.create_climb_form_widget.widget.saveClimb.setEnabled(False)
        self.create_climb_btn.setEnabled(True)
        
        # #if (self.create_climb_form_widget.climb_name == 'Climb Name') and (self.create_climb_form_widget.grade == 0) and (self.create_climb_form_widget.route == 'Route'):
        # if (self.create_climb_form_widget.climb_name != 1)\
        #     and (self.create_climb_form_widget.grade != 0):
        #     print('please populate required fields')
            
        # else:

        print('saving climb')
        with open('climbs.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            climb = [self.route,\
                self.create_climb_form_widget.widget.climb_nam.text(),\
                    self.create_climb_form_widget.widget.Grade.value()]
            writer.writerow(climb)

    def handle_cancel_create_climb(self):
        print('creating climb cancelled')
        self.create_climb_btn.setEnabled(True)
        self.create_climb_form_widget.widget.saveClimb.setEnabled(False)
        self.create_climb_form_widget.widget.cancelcreation.setEnabled(False)
        
        self.create_climb_form_widget.widget.Grade.setValue(0)
        self.create_climb_form_widget.widget.climb_nam.setText("Climb Name")
        self.route.clear()
        
        for button in self.board_widget.hold_buttons_group.buttons():
            if button.isChecked() == True:
                button.setStyleSheet("background-color: transparent;")
                button.setChecked(False)                          
            else:
                continue
        
    
    def read_climbs_csv(self, file_path):
        data = []
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
        return data
    
    def populate_table(self, table_widget, data):
        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(len(data))
        
        for row in range(len(data)):
            for column in range(len(data[row])):
                item = QTableWidgetItem(data[row][column])
                table_widget.setItem(row, column, item)
                
    def load_climb(self, index):
        # row = index.row()
        # if row == 2:
        #     print('climb loading')
        print(index)

    # def refresh_table(self):
    #     csv_data = self.read_climbs_csv('climbs.csv')
    #     self.populate_table(csv_data)
          

