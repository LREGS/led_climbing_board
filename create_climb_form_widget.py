import os.path

from PySide6 import QtWidgets, QtCore, QtGui
from create_climb_formUI import Ui_Form

class CreateClimbForm(QtWidgets.QWidget):
    def __innit__(self, parent: QtWidgets.QWidget = None) -> None:
        super(CreateClimbForm, self).__init__(parent)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.widget = Ui_Form()
        self.widget.setupUi(self)
        