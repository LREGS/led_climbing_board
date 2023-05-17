from PySide6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel 
from Climbs import Climb

class CreateClimbDlg(QDialog):
    """Create a Dialog box that initilizes the create climb sequence"""
    def __init__(self):
        super().__init__()
        self. climb = None
        self.setWindowTitle('Create Climb')        
        #Create Buttons
        Btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(Btn)
        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        #Create Layout of Dialog box
        self.layout = QVBoxLayout()
        message = QLabel("Select 'OK' and then select your desired holds")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
    
    # def create_climb(self):
    #     self.climb = Climb()
    #     print('Please Select the Holds for your route and then click save')
    #     return self.climb
        
    # def jon(self):
    #     print('Rejected')
    #     self.hide()
          
# def open_dlg_box():
#     dlg = CreateClimbDlg()
#     dlg.exec() 
            
        
    
        