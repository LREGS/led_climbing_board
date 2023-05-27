import os

from PySide6.QtCore import QFile, QIODevice, Signal
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup


from create_clmb_dlg import CreateClimbDlg
from Climbs import Climb
from open_create_clmb_dlg_box import open_clmb_dlg_box
from handle_create_climb import ClimbCreator
from load_ui_file import ui_loader
from button_group import create_button_group
from handle_save_climb import SaveClimb

def onclimb_created(climb):
    """assigns the climb object to the holder variable"""
    window.create_climb_btn.setEnabled(True)
    window.climb = climb
    print(window.climb.name)    

            
class MainWindow(QMainWindow):

             
    def __init__(self):
        
        def collect_route(button):
           #climb = Climb(route)
           hold_selected = hold_button_group.id(button)
           route.append(hold_selected)
           #climb.route.append(hold_selected)
           #print(route)
           self.climb.route = route
        #prints route through instance of a climb
           print(self.climb.route)

        super().__init__()
        
        #Holder variable for the climb object to be assigned too
        self.climb = None
        
        # Load UI file
        board_widget = self.board_widget = ui_loader\
        (os.path.join(os.path.dirname(__file__), "boardgui.ui"))


        main_layout = QVBoxLayout()
        main_layout.addWidget(self.board_widget)
        self.central_widget = QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)
        
        
        self.climb_creator = ClimbCreator()
        self.climb_creator.create_climb.connect(onclimb_created)
        
        self.climb_save = SaveClimb()
        
        hold_button_group = create_button_group(board_widget)
        
        route =[]
        
        hold_button_group.buttonClicked.connect(collect_route)
        
        def create_climb():
            self.create_climb_btn.setEnabled(False)
            self.climb_creator.handle_create_climb()
            
        def save_climb():
            self.climb_save.handle_save_climb()

        
        
        #Adds a Create Climb Button 
        self.create_climb_btn = QPushButton('Create Climb')
        self.create_climb_btn.clicked.connect(create_climb)
        main_layout.addWidget(self.create_climb_btn)
                
        #Adds a Save Climb button 
        self.save_climb_btn = QPushButton('Save Climb')
        self.save_climb_btn.clicked.connect(save_climb)
        main_layout.addWidget(self.save_climb_btn)
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    

