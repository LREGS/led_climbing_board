import os.path

from PySide6 import QtWidgets, QtCore, QtGui
from create_climb_formUI import Ui_Form

class CreateClimbForm(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None) -> None:
        super(CreateClimbForm, self).__init__(parent)
        self.widget = Ui_Form()
        self.widget.setupUi(self)
        
 
        self.climb_name = self.widget.climb_nam.text()
        self.grade = self.widget.Grade.value()
        self.route = self.widget.textEdit.toPlainText()