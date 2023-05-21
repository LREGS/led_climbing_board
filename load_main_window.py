from PySide6.QtWidgets import QVBoxLayout, QWidget
from PySide6.QtUiTools import QUiLoader
from load_main_window import ui_loader
import os

board_widget = board_widget = ui_loader\
        (os.path.join(os.path.dirname(__file__), "boardgui.ui"))
        
        
def set_main_layout(board_widget):
    main_layout = QVBoxLayout()
    main_layout.addWidget(board_widget)
    central_widget = QWidget()
    central_widget.setLayout(main_layout)
    return central_widget   

set_main_layout(board_widget)
