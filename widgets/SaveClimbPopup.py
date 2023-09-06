import json

from ui_py_files.save_climb_popup_widget import Ui_input_climb_data
from configuration_copy import Climbs

from PySide6.QtWidgets import QDialog

class SaveClimbPopup(QDialog):
    def __init__(self, route, db: Climbs= None, parent: QDialog = None) -> None:
        super(SaveClimbPopup, self,).__init__(parent)

        self.widget = Ui_input_climb_data()
        self.widget.setupUi(self)

        self.db = db
        self.route = route

        self.widget.buttonBox.accepted.connect(self.save_climb)

    def save_climb(self):
        if len(self.route) > 2:
            self.db.add_climb(self.widget.climb_name.text(), self.route, int(self.widget.grade.value()))
        else:
            print("Climb must contain 2 holds or more")