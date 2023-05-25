from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel,\
                              QLineEdit

from open_save_clmb_dlg import open_save_clmb_dlg_box
from open_name_and_grade_dlg_box import get_name_grade

class SaveClimb(QObject):
    """Handles Saving of the climb"""
    
    def __init__(self):
        self.climb_grade = None
        self.climb_name = None
        
    
    
    def handle_save_climb(self):
        
        grade, name = open_save_clmb_dlg_box()
        
        if grade and name:
           self.climb_grade = grade
           self.climb_name = name
        else:
            print('no name')
        
            
            
        
    

# def open_nameGrade_dlg():
#     dlg = NameGradeInput()
#     results = dlg.exec()