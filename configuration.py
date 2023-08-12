import sqlite3

from Singleton import Singleton


class Configuartion(metaclass=Singleton):
    def __init__(self):
        self.cx = sqlite3.connect("users.db")
        self.cu = self.cx.cursor()

    def set_up_config_db(self):
        self.cu.execute( "CREATE TABLE IF NOT EXISTS  users(username, password)")

    def add_user(self, username, password):
        self.cu.execute("INSERT INTO users VALUES(?,?)", ((username, password)))        

    def get_users(self):
        for row in self.cu.execute("SELECT * FROM users"):
            print(row)

    def get_password(self):
        for row in self.cu.execute("SELECT password FROM users"):
            print(row)
    
    def check_username(self, username):
        for row in self.cu.execute("SELECT username FROM users WHERE username = VALUE(?)", (username)):
            if row:
                print('row')
            elif row == None:
                print('no')
            
database = Configuartion()
database.set_up_config_db()
# database.get_users()

database.check_username('William')

