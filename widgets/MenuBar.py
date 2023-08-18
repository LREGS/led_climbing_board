from PySide6.QtWidgets import QMenuBar, QMenu, QPushButton

from widgets.SignUpForm import SignUpForm
from widgets.SignInForm import SignInForm

class MenuBar (QMenuBar):
    def __init__(self): 
        QMenuBar.__init__(self)

        self.signup = self.addAction('Sign Up')
        self.signup.triggered.connect(self.onsign_up_attempt)

        self.logged_user = QMenu()
        self.logged_user.setTitle('username')

        self.addMenu(self.logged_user)

        self.addMenu(self.create_profile_menu('One'))
        self.addMenu(self.create_profile_menu('Two'))
        self.addMenu(self.create_profile_menu('Three'))
        
        self.addMenu(self.logged_user)

    def create_profile_menu(self, profile_number):
        profile = QMenu()
        profile.setTitle(f'Profile {profile_number}')
        login_attempt = profile.addAction('Login')
        login_attempt.triggered.connect(self.onlogin_attempt)
        return profile
    
    def logged_in_user_button(self):
        logged_user = QPushButton()
        logged_user.setText('username')

    def create_user_account(self):
        signUp = QMenu()
        signUp.setTitle('SignUp')
        sign_up_attempt = signUp.addAction('Sign Up')
        sign_up_attempt.triggered.connect(self.onsign_up_attempt)
        return signUp

    def onsign_up_attempt(self):
        sign_up = SignUpForm()
        sign_up.exec()

    def onlogin_attempt(self):
        sign_in = SignInForm()
        sign_in.exec()
        