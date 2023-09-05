import sqlite3

from Singleton import Singleton

class DatabaseManeger(metaclass= Singleton):
    def __init__(self):
        self.db = sqlite3.connect("users.db")
        self.cursor = self.get_cu()

    def get_cu(self):
        cu = self.db.cursor()
        return cu
    
    def do_commit(self):
        self.db.commit()

class UserAccountTable:
    def __init__(self):
        self.db = DatabaseManeger()
        self.cursor = db.cursor

    def create_table(self):
        

class Configuartion(metaclass=Singleton):
    def __init__(self):
        self.cx = sqlite3.connect("users.db")
        self.cu = self.cx.cursor()

    def build_users_table(self):
        self.cu.execute( "CREATE TABLE IF NOT EXISTS  users(username, password)")

    def add_user(self, username, password):
        if self.check_username(username):
            print('user exists')
        else:
            print('adding user')    
            self.cu.execute("INSERT INTO users VALUES(?,?)", ((username, password,)))        

    def get_users(self):
        for row in self.cu.execute("SELECT * FROM users"):
            print(row)

    def get_password(self):
        for row in self.cu.execute("SELECT password FROM users"):
            print(row)
    
    def check_username(self, username):
        self.cu.execute('SELECT exists(select 1 from users where username = ?)', (username,))
        exists = self.cu.fetchone()[0]
        if exists:
            return True
        else:
            return False

    def check_password(self, password):
        self.cu.execute('SELECT exists(select 1 from users where password = ?)', (password,))
        exists = self.cu.fetchone()[0]
        if exists:
            return True
        else:
            return False
        
    # def alter_table(self):
    #     self.cu.execute("ALTER TABLE users DROP COLUMN user_id")
    #     self.cx.commit

db = Configuartion()
db.build_users_table()
