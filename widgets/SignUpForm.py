from PySide6.QtWidgets import QDialog

from ui_py_files.signupPopupUI import Ui_Dialog

class SignUpForm(QDialog):
    def __init__(self, parent: QDialog = None) -> None:
        super(SignUpForm, self).__init__(parent)    

        self.widget = Ui_Dialog()
        self.widget.setupUi(self)

        self.widget.buttonBox.accepted.connect(self.signup_attempted)
        self.widget.buttonBox.rejected.connect(self.signup_cancelled)

    def signup_attempted(self):
        print('no')

    def signup_cancelled(self):
        print('yes')