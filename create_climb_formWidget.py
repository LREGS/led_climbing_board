from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout, QButtonGroup

from create_climb_formUI import Ui_Form


class CreateClimbForm(QtWidgets.QWidget):
    def __init__(self, parent:QtWidgets.QWidget) -> None:
        super(CreateClimbForm, self).__init__(parent)
        self.widget = Ui_Form
        self.widget.setupUi(self)