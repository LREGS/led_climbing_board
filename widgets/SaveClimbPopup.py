import json
import pickle


from tools.JsonHandler import JsonHanlder as js
from ui_py_files.save_climb_popup_widget import Ui_input_climb_data
from configuration_copy import Climbs

from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal

class SaveClimbPopup(QDialog):
    SaveCancelled = Signal()
    def __init__(self, route, db: Climbs= None, parent: QDialog = None) -> None:
        super(SaveClimbPopup, self,).__init__(parent)

        self.widget = Ui_input_climb_data()
        self.widget.setupUi(self)

        self.db = db
        self.route = route

        self.widget.buttonBox.accepted.connect(self.save_climb)
        self.widget.buttonBox.rejected.connect(self.save_cancelled)

    def save_climb(self):
        if len(self.route) > 2 and self.widget.climb_name.text():
            
        #should this be seperated? and should there be a seperate function for saving 
        #route to json maybe? And the save climb just calls two functions?
        #so threading???
            new_list = pickle.dumps(self.route)
            self.db.add_climb(self.widget.climb_name.text(), new_list, int(self.widget.grade.value()))

            
            routes_path = "data/routes.json"
            data = js.openJson(routes_path)
            rt = {self.widget.climb_name.text(): self.route}
            data.append(rt)

            js.writeJson(data, routes_path)


            
        else:
            print("Climb must contain 2 holds or more") 
    
    def save_cancelled(self):
        self.SaveCancelled.emit()

