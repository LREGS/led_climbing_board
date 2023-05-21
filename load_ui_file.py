from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

def ui_loader(file_path):
    loader = QUiLoader()
    ui_file = QFile(file_path)
    
    if ui_file.open(QIODevice.ReadOnly):
        ui = loader.load(ui_file)
        ui_file.close()
        return ui
    return None