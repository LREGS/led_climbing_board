from PySide6.QtCore import QObject, Signal
from PySide6 import QtCore
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup
import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice


class Climb():
    hold_buttons = None
    #hold_selected = Signal(int)
    """Creates a Climb"""
    def __init__(self):
        
        #trying to define board_widet in here instead? think its working
        ui_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "boardgui.ui"))
        loader = QUiLoader()
        ui_file = QFile(ui_file_path)
        ui_file.open(QIODevice.ReadOnly)
        board_widget = self.board_widget = loader.load(ui_file)
        
        self.climb = {'route' : []}
        self.hold_buttons = QButtonGroup()
    def hold_buttons_f(self):
        for i in range(1, 28):
            hold = self.board_widget.findChild(QPushButton, f'hold{i}')
            self.hold_buttons.addButton(hold, i)
                
    def handle_hold_selection(self,button, hold_buttons):
        """Stores the desired holds for the climb into a dictionary"""
        hold_selected = hold_buttons.id(button)
        print(hold_selected)
        
        
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
    
    
