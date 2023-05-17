from create_clmb_dlg import CreateClimbDlg
from PySide6.QtWidgets import QDialog
from Climbs import Climb

def open_clmb_dlg_box():
    """Creates an instance of climb and opens the create climb dialog box"""
    dlg = CreateClimbDlg()
    result = dlg.exec()
            
    if result == QDialog.Accepted:
        climb = Climb('William')
        print('Please Select the Holds for your route and then click save')
        return climb
    else:
        print('You clicked cancel')