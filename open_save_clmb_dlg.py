from PySide6.QtWidgets import QDialog
from checks_button_action_dlg import CheckButtonActionDlg

def open_save_clmb_dlg_box():
    
    dlg = CheckButtonActionDlg()
    result = dlg.exec()
    
    if result == QDialog.Accepted:
        return True 
    else:
        print('Climb aborted')
        return False

