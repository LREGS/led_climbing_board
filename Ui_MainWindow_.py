import os

from PySide6.QtWidgets import QVBoxLayout, QWidget 
from load_ui_file import ui_loader

class Ui_MainWindow(object):
    def setupUI(self, MainWindow):
    #    self.board_widget = ui_loader\
    #    (os.path.join(os.path.dirname(__file__), "boardgui.ui"))
    #    self.main_layout = QVBoxLayout() 
    #    self.main_layout.addWidget(self.board_widget)
       self.central_widget = QWidget(MainWindow) 
       MainWindow.setCentralWidget(self.central_widget)
