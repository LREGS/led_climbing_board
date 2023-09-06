from PySide6.QtWidgets import QMenuBar, QMenu, QPushButton, QDialog
from PySide6.QtCore import Signal

from widgets.SignUpForm import SignUpForm
from widgets.SignInForm import SignInForm
from configuration_copy import UserAccountTable
class MenuBar (QMenuBar):

    SendUsername = Signal(str)

    def __init__(self, db: UserAccountTable= None): 
        QMenuBar.__init__(self)
        
        self.db = db

        self.signup = self.addAction('Sign Up')
        self.signup.triggered.connect(self.onsign_up_attempt)

        self.username = None



        # self.sign_in_form = SignInForm()
        # self.sign_in_form.SendUsername.connect(self.emit_username)

    #     self.addMenu(self.create_profile_menu('One'))
    #     self.addMenu(self.create_profile_menu('Two'))
        
    # def create_profile_menu(self, profile_number):
    #     profile = QMenu()
    #     profile.setTitle(f'Profile {profile_number}')
    #     login_attempt = profile.addAction('Login')
    #     login_attempt.triggered.connect(self.onlogin_attempt)
    #     return profile

    def create_user_account(self):
        signUp = QMenu()
        signUp.setTitle('SignUp')
        sign_up_attempt = signUp.addAction('Sign Up')
        sign_up_attempt.triggered.connect(self.onsign_up_attempt)
        return signUp

    def onsign_up_attempt(self):
        sign_up = SignUpForm(self.db)
        sign_up.exec()

    # def onlogin_attempt(self):
    #     self.sign_in_form.exec()
    
    def emit_username(self, username):
        self.SendUsername.emit(username)
