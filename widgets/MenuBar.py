from PySide6.QtWidgets import QMenuBar, QMenu

from widgets.SignUpForm import SignUpForm
from widgets.SignInForm import SignInForm

class MenuBar (QMenuBar):
    def __init__(self): 
        QMenuBar.__init__(self)

        self.signup = self.addAction('Sign Up')
        self.signup.triggered.connect(self.onsign_up_attempt)

        self.addMenu(self.create_profile_menu('One'))
        self.addMenu(self.create_profile_menu('Two'))
        self.addMenu(self.create_profile_menu('Three'))

    def create_profile_menu(self, profile_number):
        profile = QMenu()
        profile.setTitle(f'Profile {profile_number}')
        login_attempt = profile.addAction('Login')
        login_attempt.triggered.connect(self.onlogin_attempt)
        return profile

    def create_user_account(self):
        signUp = QMenu()
        signUp.setTitle('SignUp')
        sign_up_attempt = signUp.addAction('Sign Up')
        sign_up_attempt.triggered.connect(self.onsign_up_attempt)
        return signUp

    def onsign_in_attempt(self):
        print('whats ur login mayyte')

    def onsign_up_attempt(self):
        sign_up = SignUpForm()
        sign_up.exec()

    def onlogin_attempt(self):
        sign_in = SignInForm()
        sign_in.exec()
        