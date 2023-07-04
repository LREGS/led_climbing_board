import os
import csv

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup
from PySide6.QtCore import QObject, Signal


from BoardWidget import BoardWidget
from create_climb_form_widget import CreateClimbForm
from create_climb_formUI import Ui_Form

class MainWidget(QWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super(MainWidget, self).__init__(parent)
        
        #print statements need adding to a dlg box within the ui and not
        #printing in console
        
        self.main_layout = QVBoxLayout(self)
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
                
        self.main_layout.addWidget(self.board_widget)
        self.main_layout.addWidget(self.create_climb_btn)        
        self.main_layout.addWidget(self.create_climb_form_widget)  

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
        self.board_widget.toggle_hold_buttons(False)

        
          

