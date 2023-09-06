import sqlite3

from Singleton import Singleton

class DatabaseManager(metaclass= Singleton):
    def __init__(self):
        self.db = sqlite3.connect("userdata.db")
        self.cursor = self.db.cursor()
    
    def commit(self):
        self.db.commit()
    
    def close(self):
        self.db.close()

class UserAccountTable:
    def __init__(self):
        self.db = DatabaseManager()
        self.cursor = self.db.cursor

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(user_ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")

    def add_user(self, username, password):
        if self.check_username(username):
            print("User exists")
        else:
            self.cursor.execute("INSERT INTO users(username, password) VALUES(?,?)", ((username, password,)))
    
    def check_username(self, username):
        self.cursor.execute("SELECT EXISTS(select 1 from users where username = ?)", (username, ))
        exists = self.cursor.fetchone()[0]
        if exists:
            return True
        else:
            return False

    def check_password(self, password):
        self.cu.execute('SELECT exists(select 1 from users where password = ?)', (password,))
        exists = self.cursor.fetchone()[0]
        if exists:
            return True
        else:
            return False


class Climbs:
    def __init__(self):
        self.db = DatabaseManager()
        self.cursor = self.db.cursor
        

    #might want to cache the climbs so it makes it quicker to query them 
    #or use threading to make sure gui is responsive during the time the database takes to querry 
    def create_table(self):
        self.cursor.execute(\
        "CREATE TABLE IF NOT EXISTS climbs(\
        climbs_ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        climb_name VARCHAR(255) NOT NULL,\
        route TEXT NOT NULL,\
        grade INTEGER)")
    
    def add_climb(self, name, route, grade):
        self.cursor.execute("INSERT INTO climbs(climb_name, route, grade) VALUES(?, ?, ?)",(name, route, grade))
        self.db.commit()
        self.db.close()

class ClimbsHistory:
    def __init__(self):
        self.db = DatabaseManager()
        self.cursor = self.db.cursor
    
    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS ClimbsHistory(\
            user_id INTEGER,\
            climb_id INTEGER,\
            status TEXT )"
        )
        
    def get_sends(self):
        return 
        #get list of the users sends

    def get_projects(self):
        return 
        #get list of the users project 
    