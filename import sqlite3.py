import sqlite3

class Configuartion():
    def __init__(self):
        # self.db_file_path = 'data/test.db'
        # self.set_up_config_db()
        # self.users = []
        self.cx = sqlite3.connect("test_db.db")
        self.cu = self.cx.cursor()

    def set_up_config_db(self):
        self.cu.execute( "CREATE TABLE IF NOT EXISTS  users(username, password)")


    def add_user(self, username, password):
        self.cu.execute("INSERT INTO users VALUES(?,?)", ((username, password)))
        

    def get_users(self):
        for row in self.cu.execute("SELECT username FROM users"):
            print(row)

    def get_password(self):
        for row in self.cu.execute("SELECT password FROM users"):
            print(row)
    

        
database = Configuartion()
database.set_up_config_db()
database.get_users()
database.get_password()
