import os 

import bcrypt
from PySide6.QtWidgets import QDialog, QDialogButtonBox
from PySide6.QtCore import Signal, QObject

from ui_py_files.signinwindow import Ui_Dialog

from configuration import Configuartion

class SignInForm(QDialog):
    SendUsername = Signal(str)
    def __init__(self, parent: QDialog = None) -> None:
        super(SignInForm, self).__init__(parent)

        self.widget = Ui_Dialog()
        self.widget.setupUi(self)
        self.widget.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        
        self.widget.buttonBox.accepted.connect(self.verify_credentials)
        self.database = Configuartion()

    username_signal = Signal(str)


    def verify_credentials(self):
        print('working')
        if self.database.check_username(self.widget.username_input.text())\
        and self.database.check_password( self.widget.password_input.text()):
            self.SendUsername.emit(self.widget.username_input.text())
        else:
            print('Invalid user login')
