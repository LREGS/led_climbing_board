from PySide6.QtCore import QObject, Signal
from open_save_clmb_dlg import open_save_clmb_dlg_box

#[] open dialogue box to get name and grade
#[] add attributes to climb that are recieved from user

class SaveClimb(QObject):
    """Handles Saving of the climb"""
    
    def handle_save_climb():
        
        save_check = open_save_clmb_dlg_box()
        
        if save_check:
            print('please add name and grade')
            
        else:
            print('nothign')
        
       