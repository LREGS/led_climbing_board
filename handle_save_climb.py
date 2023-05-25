from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel,\
                              QLineEdit

from open_save_clmb_dlg import open_save_clmb_dlg_box
from open_name_and_grade_dlg_box import get_name_grade

class SaveClimb(QObject):
    """Handles Saving of the climb"""
    
    def handle_save_climb(self):
        
        name_climb_input = open_save_clmb_dlg_box()
        
        if name_climb_input:
            print('gay')            
        else:
            print('Climb Aborted')
    

# def open_nameGrade_dlg():
#     dlg = NameGradeInput()
#     results = dlg.exec()