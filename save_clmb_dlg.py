from PySide6.QtWidgets import QDialog, QLineEdit, QSpinBox                         

TODO
[] 

class SaveClimbDlg(QDialog):
    def __inint__(self):
        super().__init__()
        
        # def checks_climb_save()
        
        self.setWindowTitle('Save Climb')
        
        self.dlg = QDialog()
        self.climb_name = QLineEdit()
        self.climb_grade = QSpinBox()
        