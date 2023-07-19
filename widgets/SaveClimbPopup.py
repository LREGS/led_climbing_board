from ui_py_files.saved_climbs_table_ui import Ui_Form

from PySide6.QtWidgets import QWidget

class SaveClimbPopup(QWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super(SaveClimbPopup, self).__init__(parent)

        self.widget = Ui_Form()
        self.widget.setupUI(self)
