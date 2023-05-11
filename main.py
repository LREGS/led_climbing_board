from PySide6.QtCore import QFile, QIODevice
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog
import os
from create_clmb_dlg import CreateClimbDlg
import time

class State:
    """Tracks the current state of the UI to determine behaviour"""
    def __init__(self):
        #Checks whether the user is trying to create a climb
        self.creation_actv = False 

class Climb():
    def __init__(self, state):
        self.climb = {'route' : []}
        self.state = state
                
    def handle_hold_selection(self):
        """Stores the desired holds for the climb into a dictionary"""
        hold_name = self.sender().objectName()
        self.climb['route'].append(hold_name)
        print(hold_name)
    
    def assign_start_holds(self):
        print('n/a')
    
    def assign_finish_holds(self):
        print('n/a')
    
    def assign_grade(self):
        print('n/a')
    
    def add_rating(self):
        print('n/a')
    
    def write_to_csv(self, filename):
        print('n/a')
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Sets the main windows state
        self.state = State()

        # Load UI file
        ui_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "boardgui.ui"))
        loader = QUiLoader()
        ui_file = QFile(ui_file_path)
        ui_file.open(QIODevice.ReadOnly)
        self.board_widget = loader.load(ui_file)
        # Close the file
        ui_file.close()    
           

    

        # Add to main windows layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.board_widget)
        self.central_widget = QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)
            
        
        
        #Adds Buttons for Holds
        board_holds = []
        for i in range(1, 28):
            holds = "hold{}".format(i)
            hold = self.board_widget.findChild(QToolButton, holds)
            board_holds.append(hold)
            hold.raise_()
            #hold.clicked.connect(self.hold_selected)
            #Checks whether the user is trying to create a climb
            climb = Climb(self.state)
            hold.clicked.connect(Climb.handle_hold_selection)
              
        
        #Adds a Create Climb Button 
        self.create_climb_btn = QPushButton('Create Climb')
        main_layout.addWidget(self.create_climb_btn)
        #Slot to link in to create_climbs
        self.create_climb_btn.clicked.connect(self.create_climbs_state)
        
        #Adds a Save Climb button 
        self.save_climb_btn = QPushButton('Save Climb')
        main_layout.addWidget(self.save_climb_btn)
        
    
    def create_climbs_state(self):
        """Initiates state in which hold buttons are active assuming user 
            clicks ok"""
        dlg = CreateClimbDlg()
        
        #If user presses ok start tracking input
        if dlg.exec():
            self.state.creation_actv = True
        else:
            #needs to link with the save climb button click to stop the tracking
            self.state.creation_actv = False
        
        #Isolates the UI state to allow user to create climb    
        self.create_climb_btn.setEnabled(False)
    

        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
