
import os

from PySide6.QtWidgets import QVBoxLayout

from load_ui_file import ui_loader 
from button_group import create_button_group


"""Add ui components to this file (buttons etc)"""

class UiBoardWidget(object):
    def setupUi(self, parent):
        self.board_widget = ui_loader\
        (os.path.join(os.path.dirname(__file__), "boardgui.ui"))

        # self.main_layout = QVBoxLayout()
        # self.main_layout.addWidget(self.board_widget)
        # self.setLayout(self.main_layout)
        
        #Add buttons
        self.hold_buttons_group = create_button_group(self.board_widget)
        parent.layout().addWidget(self.board_widget)
        
        """follow ui_queue_ui to create seperate widget that 
        represents the board widget which will be a class of functions that 
        will interact with the elements of the ui defined within BoardWidgetUi
        and then added to the main_widget of the MainWindow of the app"""
        