from ui_py_files.save_climb_popup_widget import Ui_input_climb_data

from PySide6.QtWidgets import QDialog

class SaveClimbPopup(QDialog):
    def __init__(self, route, parent: QDialog = None) -> None:
        super(SaveClimbPopup, self,).__init__(parent)

        self.widget = Ui_input_climb_data()
        self.widget.setupUi(self)

        # self.widget.buttonBox.accepted.connect(self.climbsaved)
        # self.widget.buttonBox.rejected.connect(self.savecancelled)
        self.climb_name = None
        self.climb_grade = None
        self.climb_rating = None
        self.route = route

        self.widget.climb_name.textChanged.connect(self.updateName)
        self.widget.grade.valueChanged.connect(self.updateGrade)
        self.widget.ratingSpinBox.valueChanged.connect(self.updateRating)

    

    def climbsaved(self, route):
        print('saved')

    def savecancelled(self):
        print('cancelled')

    def updateName(self, text):
        self.climb_name = text
    
    def updateGrade(self, value):
        self.climb_grade = value
    
    def updateRating(self, value):
        self.climb_rating = value