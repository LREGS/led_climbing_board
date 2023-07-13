import os.path

from PySide6 import QtWidgets, QtCore, QtGui
from ui_py_files.create_climb_formUI import Ui_Form

class CreateClimbForm(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None) -> None:
        super(CreateClimbForm, self).__init__(parent)
        self.widget = Ui_Form()
        self.widget.setupUi(self)
        
 
        # self.climb_name = self.widget.climb_nam.text()
        # self.grade = self.widget.Grade.value()
        # self.route = self.widget.textEdit.toPlainText()
        
        self.climb_name = None
        self.grade = None
        self.route = None
        
        self.widget.climb_nam.textChanged.connect(self.updateClimbName)
        self.widget.Grade.valueChanged.connect(self.updateGrade)
        self.widget.textEdit.textChanged.connect(self.updateRoute)
        
    def updateClimbName(self, text):
        
        self.climb_name = text
        
    def updateGrade(self, value):
        self.grade = value
        
    def updateRoute(self, value):
        self.route = value