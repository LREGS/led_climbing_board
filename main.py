
from PySide6.QtCore import QFile, QIODevice, Signal
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup, QApplication

from ui_py_files.Ui_MainWindow_ import *
from widgets.MainWidget import MainWidget
            

class MainWindow(QMainWindow):        
    def __init__(self, app: QApplication = None):
        super(MainWindow, self).__init__()
        
        self.window_ = Ui_MainWindow()
        self.window_.setupUI(self)
        self.main_widget = MainWidget()
        self.setCentralWidget(self.main_widget)
        
    
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow(app)
    window.show()
    app.exec()
    

