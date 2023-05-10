from PySide6.QtCore import QFile, QIODevice
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog
import os
from create_clmb_dlg import CreateClimbDlg
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI file
        ui_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "boardgui.ui"))
        loader = QUiLoader()
        ui_file = QFile(ui_file_path)
        ui_file.open(QIODevice.ReadOnly)
        self.board_widget = loader.load(ui_file)

    

        # Add to main windows layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.board_widget)
        self.central_widget = QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)
            
        
        
        #Add Buttons on Climbs
        board_holds = []
        for i in range(1, 28):
            holds = "hold{}".format(i)
            hold = self.board_widget.findChild(QToolButton, holds)
            board_holds.append(hold)
            hold.raise_()
            hold.clicked.connect(self.hold_selected)
        
        """Getting messy here - do  I need to add a function to create buttons\
            into another module?!
            
            The buttons also look really ugly in the UI as they span the whole 
            window. Need adding into a toolbar or making in QtDesigner 
            so they don't look so dumb
            
            """
        
        
        
        #Adds a Create Climb Button 
        self.create_climb_btn = QPushButton('Create Climb')
        main_layout.addWidget(self.create_climb_btn)
        #Slot to link in to create_climbs
        self.create_climb_btn.clicked.connect(self.create_climbs)
        
        #Adds a Save Climb button 
        self.save_climb_btn = QPushButton('Save Climb')
        main_layout.addWidget(self.save_climb_btn)
       
       
       
        # Close the file
        ui_file.close()
    
    def hold_selected(self):
        print('hold selected')
    
    #could/should maybe be a class def track climb, def choose start 
    #def choose last hold def remove hold def illuminate button on click etc
    def create_climbs(self):
        """Starts tracking user input to create a climb ***POC*** """
        dlg = CreateClimbDlg()
        
        #If user presses ok start tracking input
        if dlg.exec():
            self.creation_actv = True
        else:
            #needs to link with the save climb button click to stop the tracking
            self.creation_actv = False
        
        #Isolates the UI state to allow user to create climb    
        self.create_climb_btn.setEnabled(False)
        
        while self.creation_actv:
            print('tracking clicks')
            time.sleep(2)
        #infinite loop - need to code the save climb button to stop the tracking
        
       
    
           
        
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
