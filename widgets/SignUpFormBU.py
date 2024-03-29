import os

from PySide6.QtWidgets import QDialog, QDialogButtonBox

from ui_py_files.SignUpWindowUI import Ui_Dialog

from tools.SignUpHandler import SignnUpHandler as handle
from tools.JsonHandler import JsonHanlder as json

class SignUpForm(QDialog):
    def __init__(self, parent: QDialog = None) -> None:
        super(SignUpForm, self).__init__(parent)    

        self.widget = Ui_Dialog()
        self.widget.setupUi(self)
        
        self.widget.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        
        self.login_details_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'account_logins.json')
        self.login_details_data = json.openJson(self.login_details_path)
        
        self.retyped_passwrd = self.widget.retyped_password_input.textChanged.connect(self.verify_data)
        self.password = self.widget.password_input.textChanged.connect(self.verify_data)
        self.widget.username_input.textChanged.connect(self.verify_data)
        
        self.widget.buttonBox.accepted.connect(self.signup_account)
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
    
    def signup_account(self):
        new_login_details_data = {self.widget.username_input.text()\
                                 : str(handle.encrypted_password(self.widget.password_input.text()))            
        }

        merged_data = {**self.login_details_data, **new_login_details_data}

        json.writeJson(merged_data, self.login_details_path)
