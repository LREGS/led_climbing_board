import os
import csv

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup
from PySide6.QtCore import QObject, Signal


from BoardWidget import BoardWidget
from Climbs import Climb
from create_climb_form_widget import CreateClimbForm
from create_clmb_dlg import CreateClimbDlg
from create_climb_formUI import Ui_Form
#from create_climb_formWidget import CreateClimbForm

class MainWidget(QWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super(MainWidget, self).__init__(parent)
        #add board widdget
        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)

        self.board_widget = BoardWidget()
        self.board_widget.hold_buttons.buttonClicked.connect(self.collect_route)
        
        self.create_climb_form_widget = CreateClimbForm()
        self.create_climb_form_widget.widget.saveClimb.clicked.connect(self.save_climb_data)
        
        self.create_climb_btn = QPushButton('Create Climb')
        
        self.save_climb_btn = QPushButton('Save Climb')
        
        self.main_layout.addWidget(self.board_widget)
        self.main_layout.addWidget(self.create_climb_btn)        
        self.main_layout.addWidget(self.save_climb_btn)   
        self.main_layout.addWidget(self.create_climb_form_widget)  

        self.create_climb_btn.setEnabled(True)
        self.save_climb_btn.setEnabled(False)
        
        self.route = []

    
    def collect_route(self, button):
        hold_selected = self.board_widget.hold_buttons.id(button)
        self.route.append(hold_selected)
        self.create_climb_form_widget.widget.textEdit.setPlainText(str(self.route))
        
    
    def save_climb_data(self):
        print('saving climb')
        with open('climbs.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            
            header = ['route', 'name', 'grade']
            writer.writerow(header)
            
            climb = [self.create_climb_form_widget.widget.textEdit.toPlainText(),\
                self.create_climb_form_widget.widget.climb_nam.text(),\
                    self.create_climb_form_widget.widget.Grade.value()]
            writer.writerow(climb)
          

