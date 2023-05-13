from PySide6 import QtCore
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup
import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from main import route


class Climb():
    
    """Creates a Climb"""
    def __init__(self, button):
        print(button)
    
    def route(self, button):
        #self.hold_buttons.append(id(button))
        print(button)    
 