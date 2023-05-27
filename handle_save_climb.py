from PySide6.QtCore import QObject, Signal

from open_save_clmb_dlg import open_save_clmb_dlg_box

class SaveClimb(QObject):
    """Handles Saving of the climb"""
    # climb_grade = Signal(int)
    # climb_name = Signal(str)
    name_grade = Signal(str, int)
    
    def handle_save_climb(self):
        
        grade, name = open_save_clmb_dlg_box()
        
        if grade and name:
           print(f'Your route is v{grade}, and called {name}')
        #    self.climb_grade.emit(grade)
        #    self.climb_name.emit(name)
           self.name_grade.emit(name, grade)
        else:
            print('no data')
