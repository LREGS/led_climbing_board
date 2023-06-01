
import os

from PySide6.QtWidgets import QVBoxLayout

from load_ui_file import ui_loader 

class UiBoardWidget(object):
    def setupUi(self):
        self.board_widget = ui_loader\
        (os.path.join(os.path.dirname(__file__), "boardgui.ui"))

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.board_widget)
        self.setLayout(self.main_layout)
        