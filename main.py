import sqlite3

#notes

from PySide6.QtCore import QFile, QIODevice, Signal
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup, QApplication

from ui_py_files.MainWindowUI import *
from widgets.MainWidget import MainWidget
from DBConfig import Climbs, ClimbsHistory, UserAccountTable
            

class MainWindow(QMainWindow):        
    def __init__(self, app: QApplication = None):
        super(MainWindow, self).__init__()

        self.ClimbsDatabase = Climbs()
        self.ClimbsDatabase.create_table()

        self.ClimbsHistory = ClimbsHistory()
        self.ClimbsHistory.create_table()

        self.UserAccountDatabase = UserAccountTable()
        self.UserAccountDatabase.create_table()


        self.window_ = Ui_MainWindow()
        self.window_.setupUI(self)
        self.main_widget = MainWidget(self.ClimbsDatabase, self.ClimbsHistory, self.UserAccountDatabase)
        self.setCentralWidget(self.main_widget)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow(app)
    window.show()
    app.exec()  
    
