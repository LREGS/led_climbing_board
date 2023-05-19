from PySide6.QtCore import QFile, QIODevice, Signal
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup
import os

from create_clmb_dlg import CreateClimbDlg
from Climbs import Climb
from open_create_clmb_dlg_box import open_clmb_dlg_box

                
class MainWindow(QMainWindow):

             
    def __init__(self):
        
        def collect_route(button):
           climb = Climb(route)
           hold_selected = button_group.id(button)
           route.append(hold_selected)
           #climb.route.append(hold_selected)
           #print(route)
           climb.route = route
        #prints route through instance of a climb
           print(climb.route)
        
            #Adds Buttons for Holds
        def create_btn_group(boardWidget):
            hold_buttons = QButtonGroup()
            for i in range(1, 28):
                hold = boardWidget.findChild(QPushButton, f'hold{i}')
                hold_buttons.addButton(hold, i)
            return hold_buttons
      
        super().__init__()
        
        #Holder variable for the climb object to be assigned too
        self.climb = None
        
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
    
        #Create Button Group for Holds
        button_group = create_btn_group(board_widget)
        
        #Placeholder for the route list
        route =[]

        #Connects the buttons to the collect_route slot
        button_group.buttonClicked.connect(collect_route)
        
        #Adds a Create Climb Button 
        self.create_climb_btn = QPushButton('Create Climb')
        main_layout.addWidget(self.create_climb_btn)
        
        def handle_create_climb():
            """Gets climb as object from open_clmb_dlg_box and prints name"""
            self.climb = open_clmb_dlg_box()
           
            if self.climb is not None:
                print(self.climb.name)
            else:
                print('no climb')       
        
        #Slot to link in to create_climbs
        #self.create_climb_btn.clicked.connect(open_clmb_dlg_box)
        self.create_climb_btn.clicked.connect(handle_create_climb)
        
        def change_climb_name(self):
            if self.climb:
                self.climb.name = 'bas'
            else:
                print('error 404')
            
        print(change_climb_name(self))
                
        #Adds a Save Climb button 
        self.save_climb_btn = QPushButton('Save Climb')
        main_layout.addWidget(self.save_climb_btn)
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()