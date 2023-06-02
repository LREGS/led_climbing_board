from create_clmb_dlg import CreateClimbDlg
from PySide6.QtWidgets import QDialog
from Climbs import Climb

def open_clmb_dlg_box():
    """Creates an instance of climb and opens the create climb dialog box"""
    dlg = CreateClimbDlg()
    result = dlg.exec()
            
    if result == QDialog.Accepted:
        route = return_route()
        print('Please Select the Holds for your route and then click save')
        return route
    else:
        print('You clicked cancel')
        
#if Qdialog accepted collect route while save_climb_button.setEnabled(True)
#this should record the route until the save climb button has been pressed