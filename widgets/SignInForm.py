import os 

import bcrypt
from PySide6.QtWidgets import QDialog, QDialogButtonBox

from ui_py_files.signinwindow import Ui_Dialog
from tools.JsonHandler import JsonHanlder as json

class SignInForm(QDialog):
    def __init__(self, parent: QDialog = None) -> None:
        super(SignInForm, self).__init__(parent)

        self.widget = Ui_Dialog()
        self.widget.setupUi(self)
        self.widget.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        
        self.widget.username_input.textChanged.connect(self.verify_credentials)


        self.login_data_path = self.login_details_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'account_logins.json')
        self.login_details_data = json.openJson(self.login_details_path)


    def verify_credentials(self):
        if self.widget.username_input.text() in self.login_details_data:
            password = self.login_details_data[self.widget.username_input.text()]
            encoded_stored_pw = password.encode('utf-8')
            encoded_entered_pw = self.widget.password_input.text().encode('utf-8')
            if bcrypt.checkpw(encoded_entered_pw, encoded_stored_pw):
                print('login successful')