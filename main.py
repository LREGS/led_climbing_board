import os

from PySide6.QtCore import QFile, QIODevice, Signal
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup, QApplication


from create_clmb_dlg import CreateClimbDlg
from Climbs import Climb
from open_create_clmb_dlg_box import open_clmb_dlg_box
from handle_create_climb import ClimbCreator
from load_ui_file import ui_loader
from button_group import create_button_group
from handle_save_climb import SaveClimb
from Ui_MainWindow_ import *
from MainWidget import MainWidget

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
    def __init__(self, app: QApplication = None):
        super(MainWindow, self).__init__()
        
        # self.climb = None
        
        # self.board_widget = ui_loader\
        # (os.path.join(os.path.dirname(__file__), "boardgui.ui"))

        # self.main_layout = QVBoxLayout()
        # self.main_layout.addWidget(self.board_widget)
        # self.central_widget = QWidget()
        # self.central_widget.setLayout(self.main_layout)
        # self.setCentralWidget(self.central_widget)
        self.window_ = Ui_MainWindow()
        self.window_.setupUI(self)
        self.main_widget = MainWidget()
        self.setCentralWidget(self.main_widget)
        
        
    #     self.climb_creator = ClimbCreator()
    #     self.climb_creator.create_climb.connect(onclimb_created)
        
    #     self.climb_save = SaveClimb()
    #     """"not sure why this isn't currently working"""
    #     #self.climb_save.name_grade.connect(onclimb_created)
        
    #     self.hold_button_group = create_button_group(self.board_widget)
        
    #     self.route =[]
        
    #     self.hold_button_group.buttonClicked.connect(self.collect_route)
        
    #     self.create_climb_btn = QPushButton('Create Climb')
    #     self.create_climb_btn.clicked.connect(self.create_climb)
    #     self.main_layout.addWidget(self.create_climb_btn)
                
    #     self.save_climb_btn = QPushButton('Save Climb')
    #     self.save_climb_btn.clicked.connect(self.save_climb)
    #     self.main_layout.addWidget(self.save_climb_btn)
        
    # def  collect_route(self, button):
    #     hold_selected = self.hold_button_group.id(button)
    #     self.route.append(hold_selected)
    #     self.climb.route = self.route
    #     print(self.climb.route)
        
    # def create_climb(self):
    #     self.create_climb_btn.setEnabled(False)
    #     self.climb_creator.handle_create_climb()
    
    # def save_climb(self):
    #     self.climb_save.handle_save_climb()
    
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow(app)
    window.show()
    app.exec()
    

