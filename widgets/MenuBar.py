from PySide6.QtWidgets import QMenuBar, QMenu
from PySide6.QtCore import Signal

from widgets.SignUpForm import SignUpForm
from DBConfig import UserAccountTable
class MenuBar (QMenuBar):

    SendUsername = Signal(str)

    def __init__(self, db: UserAccountTable= None): 
        QMenuBar.__init__(self)
        
        self.db = db

        self.signup = self.addAction('Sign Up')
        self.signup.triggered.connect(self.onsign_up_attempt)

        self.username = None

    def create_user_account(self):
        signUp = QMenu()
        signUp.setTitle('SignUp')
        sign_up_attempt = signUp.addAction('Sign Up')
        sign_up_attempt.triggered.connect(self.onsign_up_attempt)
        return signUp

    def onsign_up_attempt(self):
        sign_up = SignUpForm(self.db)
        sign_up.exec()
    
    def emit_username(self, username):
        self.SendUsername.emit(username)
