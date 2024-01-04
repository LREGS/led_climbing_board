from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal

"""Unfinished class trying to make the hold buttons the actual images of the buttons, rather than the current ugly squares."""

class clickableLabel(QLabel):

    click = Signal()
    def __init__(self, parent=None):
        super(clickableLabel, self).__init__(parent)
        #None = unchecked, True = Checked
        self.isChecked = False

    def mouseReleaseEvent(self, event):
        self.click.emit()
        self.toggleChecked()

    def toggleChecked(self):
        if self.isChecked:
            self.isChecked = False
        else:
            self.isChecked = True



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
        
