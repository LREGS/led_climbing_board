from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel 

class CheckButtonActionDlg(QDialog):
    """Checks if user meant button click with yes/no"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle(str('title'))   
             
        Btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(Btn)
        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        self.layout = QVBoxLayout()
        message = QLabel(str('label'))
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

        