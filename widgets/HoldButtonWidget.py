import sys
from PySide6.QtGui import QMouseEvent, QPixmap, QPainter
from PySide6.QtWidgets import QAbstractButton, QApplication, QWidget, QHBoxLayout, QLabel, QMainWindow
from PySide6.QtCore import Signal

class clickableLabel(QLabel):
    """Now I wont have the checked/unchecked functionality 
    that I rely on to control my view model for the buttons
    so I will need to devise a new way.
    
    I just think opn every action (create/load) climb we wipe 
    the ui 
    
    and then On MouseRelease we should make it switch between two 
    pixmaps - one is a button that represents selected (aurora around 
    hold) and one is the standard pixmap that just shows the button"""
    
    click = Signal()
    def __init__(self, parent=None):
        super(clickableLabel, self).__init__(parent)

    def mouseReleaseEvent(self, event):
        self.click.emit()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = QMainWindow()
#     layout = QHBoxLayout()
 

#     label = clickableLabel()
#     imagePath = "/home/william/Desktop/led_climbing_board/board.jpeg"
#     pixmap = QPixmap(imagePath)
#     if not pixmap.isNull():
#         print('added pixmap')
#         label.setPixmap(pixmap)
#     else:
#         print('no pixmap')
#     label.setFixedSize(pixmap.size())
#     label.setVisible(True)

#     # Connect the label to a function when clicked
#     label.click.connect(lambda: print("Label clicked!"))

#     layout.addWidget(label)
#     window.setLayout(layout)
#     window.show()
#     sys.exit(app.exec_())

"""Not sure this method will work becuase I cannot promote it and use it in QtDesigner"""

# class holdButton(QAbstractButton):
#     def __init__(self,pixmap, parent=None):
#         super(holdButton, self).__init__(parent)
#         self.pixmap = pixmap

#     def paintEvent (self, event):
#         painter = QPainter(self)
#         painter.drawPixmap(event.rect(), self.pixmap)
    
#     def sizeHint(self):
#         return self.pixmap.size()
        
