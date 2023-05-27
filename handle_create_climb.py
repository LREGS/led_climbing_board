from PySide6.QtCore import QObject, Signal

from open_create_clmb_dlg_box import open_clmb_dlg_box

class ClimbCreator(QObject):
    """Handles the creation of a climb"""
    create_climb = Signal(object)
    
    def handle_create_climb(self):
        """Gets climb as object from open_clmb_dlg_box"""
        
        #climb = Climb()
        climb = open_clmb_dlg_box()
        
        if climb is not None:
            #print(climb.name)
            self.create_climb.emit(climb)
        else:
            print('no climb')   