import sqlite3

from Singleton import Singleton


class Configuartion(metaclass=Singleton):
    def __init__(self):
        self.db_file_path = 'data/test.db'
        self.set_up_config_db()
        
    def set_up_config_db(self):
        connection = sqlite3.connect(self.db_file_path)
        connection.execute('''
            CREATE TABLE IF NOT EXISTS  users(
            username TEXT,
            password TEXT
                             
            );'''
        )
        connection.commit()
        connection.close()

    def add_user(self, username, password):
        connection = sqlite3.connect(self.db_file_path)
        cursor = connection.cursor()

        cursor.execute('''INSERT INTO users(username, password)
                             VALUES(?,?)
                             ''', ((username, password))
                            )