from PySide6.QtWidgets import QDialog, QLineEdit, QSpinBox                         

#TODO
#[] create an ok/cancel dialog box to check the user wants  to save 
#[] create the dlg box that will take the climb name and climb grade as an int
#[] saved and return these values 

class SaveClimbDlg(QDialog):
    def __inint__(self):
        super().__init__()
        
        # def checks_climb_save()
        
        self.setWindowTitle('Save Climb')
        
        self.dlg = QDialog()
        self.climb_name = QLineEdit()
        self.climb_grade = QSpinBox()
        