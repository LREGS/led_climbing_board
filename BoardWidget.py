import os 

from PySide6 import QtWidgets, QtCore, QtGUi

from BoardWidgetUi import UiBoardWidget

class BoardWidget(QtWidgets.QWidget):
    def __init__(self, paretns: QtWidgets.QWidget = None) -> None:
        super(BoardWidget, self).__init__(parent)
        self.widget = UiBoardWidget()