from PySide6.QtWidgets import QDialogButtonBox, QDialog

class NameGradeInput(QDialog):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle('Climbg information')
        
        Btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            
        self.buttonBox = QDialogButtonBox(Btn)
            
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
