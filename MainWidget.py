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
        hold_selected = self.board_widget.hold_buttons_group.id(button)
        self.route.append(hold_selected)
        self.create_climb_form_widget.widget.textEdit.setPlainText\
        (str(self.route))
        
    
    def save_climb_data(self):
        print('saving climb') 
        self.create_climb_form_widget.widget.saveClimb.setEnabled(False)
        self.create_climb_btn.setEnabled(True)
        with open('climbs.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            climb = [self.create_climb_form_widget.widget.textEdit.toPlainText(),\
                self.create_climb_form_widget.widget.climb_nam.text(),\
                    self.create_climb_form_widget.widget.Grade.value()]
            writer.writerow(climb)
    
    def handle_cancel_create_climb(self):
        print('creating climb cancelled')
        self.create_climb_btn.setEnabled(True)
        self.create_climb_form_widget.widget.saveClimb.setEnabled(False)
        self.board_widget.toggle_hold_buttons(False)

        
          

