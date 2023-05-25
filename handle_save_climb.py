from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel,\
                              QLineEdit


from open_save_clmb_dlg import open_save_clmb_dlg_box
from open_name_and_grade_dlg_box import get_name_grade

#[] open dialogue box to get name and grade
#[] add attributes to climb that are recieved from user

def open_nameGrade_dlg():
    dlg = NameGradeInput()
    results = dlg.exec()


class SaveClimb(QObject):
    """Handles Saving of the climb"""
    
    def handle_save_climb(self):
        
        save_check = open_save_clmb_dlg_box()
        
        if save_check:
            name_grade_input = open_nameGrade_dlg()
            
        else:
            print('nothing')
    

class NameGradeInput(QDialog):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle('Climb information')
        
        Btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            
        self.buttonBox = QDialogButtonBox(Btn)
            
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        self.layout = QVBoxLayout()
        self.climb_name = QLineEdit()
        self.climb_name.setText('Name of Climb')
        self.layout.addWidget(self.climb_name)
