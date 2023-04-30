#end goal to create toolbar with drop down allowing a user to upload a board
#and select their holds.

#but for now I'm going to upload the photo of the board into a stacked widget 
#and manually create buttons over the holds to allow users to set climbs
import os, sys
from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
window.setGeometry(0, 0, 400, 200)

def board_photo():
    pic = QtGui.Qlabel(window)
    pic.setGeometry(10,10,100,100)
    pic.setPixmap(QtGui.QPixmap(os.getcwd() + '/Desktop/climbing_board/board_img'))

window.show()
sys.exit(app.exec_())