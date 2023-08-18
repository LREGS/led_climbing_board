import os 

import bcrypt
from PySide6.QtWidgets import QDialog, QDialogButtonBox

from ui_py_files.signinwindow import Ui_Dialog

from configuration import Configuartion

class SignInForm(QDialog):
    def __init__(self, parent: QDialog = None) -> None:
        super(SignInForm, self).__init__(parent)

        self.widget = Ui_Dialog()
        self.widget.setupUi(self)
        self.widget.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        
        self.widget.buttonBox.accepted.connect(self.verify_credentials)
        self.database = Configuartion()

        self.username = self.widget.username_input.text()
        self.password  = self.widget.password_input.text()


    def verify_credentials(self):
        if self.database.check_username(self.widget.username_input.text())\
        and self.database.check_password(self.widget.password_input.text()):
            print('logging')
        else:
            print('invalid login')
