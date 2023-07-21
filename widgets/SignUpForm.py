import PySide6.QtGui
from PySide6.QtWidgets import QDialog, QDialogButtonBox
import bcrypt

from ui_py_files.signupPopupUI import Ui_Dialog

class SignUpForm(QDialog):
    def __init__(self, parent: QDialog = None) -> None:
        super(SignUpForm, self).__init__(parent)    

        self.widget = Ui_Dialog()
        self.widget.setupUi(self)
        self.widget.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        self.widget.retyped_password_input.textChanged.connect(self.verify_data)
        self.widget.password_input.textChanged.connect(self.verify_data)
        self.widget.username_input.textChanged.connect(self.verify_data)
        
        self.widget.buttonBox.accepted.connect(self.get_details)
        self.widget.buttonBox.rejected.connect(self.signup_cancelled)

    def get_details(self):
        username = self.widget.username_input.text()
        encrypted_password = self.encrypt_password(self.widget.password_input.text())
        print(username, encrypted_password)

    def encrypt_password(self, password):
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=15))
        print(password_hash)
        return password_hash
    
    def signup_cancelled(self):
        print('yes')

    def verify_data(self):
        if self.widget.password_input.text() == self.widget.retyped_password_input.text()\
            and len(self.widget.username_input.text()) > 0:
            self.widget.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        else:
            self.widget.communication_box.setText('Passwords must match')

    def verify_username(self):
        if len(self.widget.username_input.text()) == 0:
            self.widget.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        else:
            self.widget.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)


