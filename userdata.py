import sqlite3

from Singleton import Singleton

class UserData(metaclass=Singleton):
    def __init__(self):

        self.cx = sqlite3.connect('data/userdata.db')
        self.cu = self.cx.cursor()

    def set_up_db(self):
        self.cu.execute( "CREATE TABLE IF NOT EXISTS  UserData(username, sends, projects)")
    
    def add_user(self, username):
        self.cu.execute("INSERT INTO UserData VALUES(?)", (username))

    def add_send(self, climb_name):
        self.cu.execute("INSER INTO UserData VALUES(?)", (climb_name))


