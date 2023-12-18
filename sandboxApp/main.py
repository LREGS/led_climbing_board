from PySide6.QtCore import QFile, QIODevice, Signal
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup, QApplication, QGridLayout, QWidget
from PySide6 import QtWidgets

from testBoardui import Ui_Form

class BoardWidget(QtWidgets.QWidget):
    '''Controls and represents the climbing board and the buttons that represent the holds'''
    def __init__(self, parent: QtWidgets.QWidget = None) -> None:
        super(BoardWidget, self).__init__(parent)
        self.widget = Ui_Form()
        self.setLayout(QVBoxLayout())
        self.widget.setupUi(self)

        self.setFixedSize(400,400)
        

class MainWindow(QMainWindow):        
    def __init__(self, app: QApplication = None):
        super(MainWindow, self).__init__()


        self.board = BoardWidget()
        self.setCentralWidget(self.board)
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow(app)
    window.show()
    app.exec()  
    

