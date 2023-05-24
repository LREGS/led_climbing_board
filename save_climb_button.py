from PySide6.QtWidgets import QPushButton

class SaveClimbButton:
    def __init__(self):
        self.save_climb_btn = QPushButton('Save Climb')
        
    def save_btn_pressed(self):
        self.save_climb_btn.setEnabled(False)