from PySide6.QtWidgets import QButtonGroup, QPushButton

def create_button_group(ui_file):
    button_group = QButtonGroup()
    for i in range(1, 28):
        button = ui_file.findChild(QPushButton, f'hold{i}')
        button_group.addButton(button, i)
    return button_group