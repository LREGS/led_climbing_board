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

def onclimb_created(climb, name=None, grade=None):
    """assigns the climb object to the holder variable"""
    window.create_climb_btn.setEnabled(True)
    window.climb = climb
    #print(window.climb.name)
    window.climb.name = name
    window.climb.grade = grade
    #print(window.climb)
    
# def assign_name(name):
#     window.climb.name = name

# def assign_grade(grade):
#     window.climb.grade = grade 
#     print(window.climb)   

            
class MainWindow(QMainWindow):

             
    def __init__(self):
        
        def collect_route(button):
           hold_selected = hold_button_group.id(button)
           route.append(hold_selected)
           self.climb.route = route
           print(self.climb.route)

        super().__init__()
        
        self.climb = None
        
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
        # self.climb_save.climb_grade.connect(assign_grade)
        # self.climb_save.climb_name.connect(assign_name)
        self.climb_save.name_grade.connect(onclimb_created)
        
        hold_button_group = create_button_group(board_widget)
        
        route =[]
        
        hold_button_group.buttonClicked.connect(collect_route)
        
        def create_climb():
            self.create_climb_btn.setEnabled(False)
            self.climb_creator.handle_create_climb()
            
        def save_climb():
            self.climb_save.handle_save_climb()

        
        self.create_climb_btn = QPushButton('Create Climb')
        self.create_climb_btn.clicked.connect(create_climb)
        main_layout.addWidget(self.create_climb_btn)
                
        self.save_climb_btn = QPushButton('Save Climb')
        self.save_climb_btn.clicked.connect(save_climb)
        main_layout.addWidget(self.save_climb_btn)
        
        print('dank')
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    

