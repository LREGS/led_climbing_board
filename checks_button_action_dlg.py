from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel,\
    QLineEdit
from PySide6.QtGui import QIntValidator

class CheckButtonActionDlg(QDialog):
    """Checks if user meant button click with yes/no"""
    def __init__(self):
        
        self.name = None
        self.grade = None
                
        super().__init__()
        self.setWindowTitle('Save Climb')   
             
        Btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(Btn)
        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        self.get_climb_name = QLineEdit()
        self.get_climb_name.setPlaceholderText('Name of Climb')
        
        self.get_climb_grade = QLineEdit()
        self.get_climb_grade.setPlaceholderText('Input number here')
        self.int_validator = QIntValidator() 
        self.get_climb_grade.setValidator(self.int_validator)
        
        self.get_climb_name.textEdited.connect(self.handle_climb_name)
        self.get_climb_grade.textEdited.connect(self.handle_climb_grade)
        
        
        self.layout = QVBoxLayout()
        message = QLabel('Please Type the Name and V Grade number bellow')
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.layout.addWidget(self.get_climb_name)
        self.layout.addWidget(self.get_climb_grade)
        self.setLayout(self.layout)
                
    def handle_climb_name(self, text):
        self.name = text
    
    def handle_climb_grade(self, text):
        self.grade = text

        