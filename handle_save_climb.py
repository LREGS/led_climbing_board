from PySide6.QtCore import QObject, Signal

from open_save_clmb_dlg import open_save_clmb_dlg_box

class SaveClimb(QObject):
    """Handles Saving of the climb"""
    name_grade = Signal(str, int)
    
    def __init__(self):
        self.climb_grade = None
        self.climb_name = None
    
    def handle_save_climb(self):
        
        grade, name = open_save_clmb_dlg_box()

        if grade and name:
           print(f'Your route is v{grade}, and called {name}')
           self.name_grade.emit(name, grade)
        else:
            print('no data')
