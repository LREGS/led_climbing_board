import os
import sqlite3

from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel

from ui_py_files.signupPopupUI import Ui_Dialog

from tools.SignUpHandler import SignnUpHandler as handle
from tools.JsonHandler import JsonHanlder as json
from configuration_copy import UserAccountTable
class SignUpForm(QDialog):
    def __init__(self, db: UserAccountTable = None, parent: QDialog = None) -> None:
        super(SignUpForm, self).__init__(parent)    

        self.widget = Ui_Dialog()
        self.widget.setupUi(self)

        self.db = db
        
        self.widget.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        
        self.retyped_passwrd = self.widget.retyped_password_input.textChanged.connect(self.verify_data)
        self.password = self.widget.password_input.textChanged.connect(self.verify_data)
        self.widget.username_input.textChanged.connect(self.verify_data)
        
        self.widget.buttonBox.accepted.connect(self.add_user_profile)
        self.widget.buttonBox.rejected.connect(self.signup_cancelled)

    def signup_cancelled(self):
        print('cancell pressed')

    def verify_data(self):
        password = handle.password_checker(self.widget.password_input.text(), self.widget.retyped_password_input.text())
        username = handle.username_checker(self.widget.username_input.text())

        if password and username:
            self.widget.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        else:
            self.widget.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

    def add_user_profile(self):
        
        self.db.add_user(self.widget.username_input.text(), self.widget.password_input.text())
        self.db.db.commit()

    

        