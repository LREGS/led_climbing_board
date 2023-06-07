import os

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup
from PySide6.QtCore import QObject, Signal


from BoardWidget import BoardWidget
from Climbs import Climb
from create_climb_form_widget import CreateClimbForm
from create_clmb_dlg import CreateClimbDlg
from create_climb_formUI import Ui_Form


class MainWidget(QWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super(MainWidget, self).__init__(parent)
        #add board widdget
        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)

        self.board_widget = BoardWidget()
        self.board_widget.hold_buttons.buttonClicked.connect(self.collect_route)
        
        #not sure why this isn't working as - CreateClimbFormWidget()
        self.create_climb_form_widget = QWidget()
        self.create_climb_form = Ui_Form()
        self.create_climb_form.setupUi(self.create_climb_form_widget)
        
        
        self.create_climb_btn = QPushButton('Create Climb')
        self.create_climb_btn.clicked.connect(self.begin_create_climb)
        
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
        self.create_climb_form.textEdit.setPlainText(str(self.route))
            
          
    def create_climb(self): 
        """Create a climb once all the data collection has been satisified/
        / save button pressed"""
        climb = Climb(self.board_widget.route)
        return 
    
                    
    def begin_create_climb(self):
        self.create_climb_btn.setEnabled(False)
        #while len(self.board_widget.route) == 0:
        #     self.save_climb_btn.setEnabled(False)
        #     print('please select a route')
        # else:
        #     self.save_climb_btn.setEnabled(True)
        # self.board_widget.creating_climb = True
        if self.board_widget.route:
            self.save_climb_btn.setEnabled(True)
            print(self.board_widget.route)
        else:
            self.save_climb_btn.setEnabled(False)
            dlg = CreateClimbDlg()
            #ui = Ui_Form()
            dlg.setModal(False)
            ui.setupUi(dlg)
            dlg.exec()