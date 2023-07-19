import os
import csv
import json

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup, \
QTableWidget, QGridLayout, QTableWidgetItem
from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtGui import QPalette, QColor


from widgets.BoardWidget import BoardWidget
from widgets.create_climb_form_widget import CreateClimbForm
from ui_py_files.create_climb_formUI import Ui_Form
from widgets.SavedClimbsTable import SavedClimbsTable
from data.climbs_dict import climbs_dict
from widgets.SaveClimbPopup import SaveClimbPopup

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
        
        self.create_climb_form_widget.widget.saveClimb.clicked.connect\
        (self.save_climb_data)
        self.create_climb_form_widget.widget.cancelcreation.clicked.connect\
        (self.handle_cancel_create_climb)
        
        self.create_climb_btn = QPushButton('Create Climb')
        self.create_climb_btn.clicked.connect(self.handle_create_climb)
        
        self.saved_climbs = SavedClimbsTable()
        self.saved_climbs.populate_table()
        self.saved_climbs.widget.tableWidget.cellClicked.connect(self.get_route)
   
        self.main_layout.addWidget(self.board_widget, 0,0)
        self.main_layout.addWidget(self.create_climb_btn, 1,0)  
        self.main_layout.addWidget(self.create_climb_form_widget, 0,1) 
        self.main_layout.addWidget(self.saved_climbs, 0,3)

        self.route = []
        
        
        
    def handle_create_climb(self):
        self.create_climb_btn.setEnabled(False)
        self.create_climb_form_widget.widget.saveClimb.setEnabled(True)
        self.create_climb_form_widget.widget.cancelcreation.setEnabled(True)
        self.board_widget.enable_buttons()
        self.default_board()


    def collect_route(self, button): 
        if self.create_climb_btn.isEnabled() == True:
            print('Please press create climb first')
        elif button.isChecked() == True:
            self.route.append(self.board_widget.hold_buttons_group.id(button))
            button.setStyleSheet("background-color: green;")
        else:
            self.route.remove(self.board_widget.hold_buttons_group.id(button))
            button.setStyleSheet("background-color: transparent;")


    def save_climb_data(self):
        self.create_climb_form_widget.widget.saveClimb.setEnabled(False)
        self.create_climb_btn.setEnabled(True)
        
        if self.create_climb_form_widget.climb_name and\
            self.create_climb_form_widget.grade and\
            len(self.route) > 1:
                main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   
                relative_path = 'data/climbs_dict.json'
                data_file_path = os.path.join(main_folder, relative_path)

                with open\
                (data_file_path, 'r') as f: 
                    my_dict = json.load(f)
                    
                    my_dict[self.create_climb_form_widget.climb_name] = \
                       {'route' : self.route,
                        'grade' : self.create_climb_form_widget.grade}
                                       
                with open\
                (data_file_path, 'w') as f: 
                    json.dump(my_dict, f)
                    
                self.saved_climbs.populate_table()
                
             
        else:
            print('please input climb information')
        self.defaultUi()

    def handle_cancel_create_climb(self):
        print('creating climb cancelled')
        self.defaultUi()
            
    def defaultUi(self):
        """ returns UI back to default state """
        
        self.create_climb_btn.setEnabled(True)
        self.create_climb_form_widget.widget.saveClimb.setEnabled(False)
        self.create_climb_form_widget.widget.cancelcreation.setEnabled(False)
        
        self.create_climb_form_widget.widget.Grade.setValue(0)
        self.create_climb_form_widget.widget.climb_nam.setText("Climb Name")
        self.route.clear()
        
        self.default_board()

 
        
                
    def get_route(self, row, column):
        self.defaultUi()
        climb_name = \
        self.saved_climbs.widget.tableWidget.item(row, column).text()
        
        main_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   
        relative_path = 'data/climbs_dict.json'
        data_file_path = os.path.join(main_folder, relative_path)

        with open\
        (data_file_path, 'r') as f: 
            my_dict = json.load(f)
        
        self.display_route(my_dict[climb_name]['route'])
        
        
    def display_route(self, route):
        for button in route:
            button_to_display = self.board_widget.hold_buttons_group.button(button)
            button_to_display.setStyleSheet("background-color: green;")
            
    def default_board(self):
        for button in self.board_widget.hold_buttons_group.buttons():
            button.setStyleSheet("background-color: transparent;")

    def onSavedClimbClicked(self):
        save_climb_data = SaveClimbPopup()
        save_climb_data.exec()


