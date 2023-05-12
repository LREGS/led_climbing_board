from PySide6.QtCore import QFile, QIODevice
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup
import os
from create_clmb_dlg import CreateClimbDlg, open_dlg_box
from Climbs import Climb
        
# class State:
#     """Tracks the current state of the UI to determine behaviour"""
#     def __init__(self):
#         #Checks whether the user is trying to create a climb
#         self.creation_actv = False 


# class Climb():
#     #hold_selected = Signal(int)
#     """Creates a Climb"""
#     def __init__(self):
#         self.climb = {'route' : []}
                
#     def handle_hold_selection(lf, hold_buttons, button = None,):
#         """Stores the desired holds for the climb into a dictionary"""
#         if button is not None:
#             hold_selected = hold_buttons.id(button)
#             print(hold_selected)
#         else:
#             return
            
        
#     def assign_start_holds(self):
#         print('n/a')
    
#     def assign_finish_holds(self):
#         print('n/a')
    
#     def assign_grade(self):
#         print('n/a')
    
#     def add_rating(self):
#         print('n/a')
    
#     def write_to_csv(self, filename):
#         print('n/a')        

                
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        climb = Climb()
        
        # def open_dlg_box():
        #     dlg = CreateClimbDlg()
        #     dlg.exec()

        # Load UI file
        ui_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "boardgui.ui"))
        loader = QUiLoader()
        ui_file = QFile(ui_file_path)
        ui_file.open(QIODevice.ReadOnly)
        board_widget = self.board_widget = loader.load(ui_file)
        # Close the file
        ui_file.close()    

        # Add to main windows layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.board_widget)
        self.central_widget = QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)
        
        #Adds buttons for holds 
        holds = climb.hold_buttons()
            
        #Adds Buttons for Holds
        # hold_buttons = QButtonGroup()
        # for i in range(1, 28):
        #     hold = self.board_widget.findChild(QPushButton, f'hold{i}')
        #     hold_buttons.addButton(hold, i)
        
        # def check(button):
        #     #while / after create climb button has been pressed, access 
        #     #the values of the button presses and store in dictionary
        #     #Check is now logic behind handle_hold_selection in climbs.py
        #     hold_selected = hold_buttons.id(button)
        #     print(hold_selected)
        
        # #Connects the hold_buttons button group to the check function    
        # #hold_buttons.buttonClicked.connect(climb.handle_hold_selection(hold_buttons))
        # hold_buttons.buttonClicked.connect(check)
        #Adds a Create Climb Button 
        self.create_climb_btn = QPushButton('Create Climb')
        main_layout.addWidget(self.create_climb_btn)
        #Slot to link in to create_climbs
        #self.create_climb_btn.clicked.connect(self.create_climbs_state)
        self.create_climb_btn.clicked.connect(open_dlg_box)
        #Adds a Save Climb button 
        self.save_climb_btn = QPushButton('Save Climb')
        main_layout.addWidget(self.save_climb_btn)
        

    #open dialogue 
    
    # def create_climbs_state(self):
    #     """Initiates state in which hold buttons are active assuming user 
    #         clicks ok"""
    #     dlg = CreateClimbDlg()
        
    #     #If user presses ok start tracking input
    #     if dlg.exec():
    #         self.state.creation_actv = True
    #     else:
    #         #needs to link with the save climb button click to stop the tracking
    #         self.state.creation_actv = False
        
    #     #Isolates the UI state to allow user to create climb    
    #     self.create_climb_btn.setEnabled(False)
    

        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
