#Import required packages
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('BOARD CLIMBS')
        self.setFixedHeight(800)
        self.setFixedWidth(800)
    