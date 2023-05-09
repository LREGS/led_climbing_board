from PySide6.QtCore import QFile, QIODevice
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI file
        ui_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "boardgui.ui"))
        loader = QUiLoader()
        ui_file = QFile(ui_file_path)
        ui_file.open(QIODevice.ReadOnly)
        self.board_widget = loader.load(ui_file)
    

        # Add to main windows layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.board_widget)
        self.central_widget = QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)
        """
        # Load the image
        image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "ched_board.jpg"))
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(400,400, QtCore.Qt.KeepAspectRatio)

        # Create a new QLabel and set its pixmap property
        self.label = QLabel(self.window)
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)"""
        
        
        
        #Add Buttons
        for i in range(1, 27):
            holds = "hold{}".format(i)
            hold = self.board_widget.findChild(QToolButton, holds)
            hold.raise_()
            hold.clicked.connect(self.hold_selected)
       
        # Close the file
        ui_file.close()
    
    def hold_selected(self):
        print('hold selected')
            
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
