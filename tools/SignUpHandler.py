import os 

import bcrypt 

from tools.JsonHandler import JsonHanlder as json

class SignnUpHandler:



    @staticmethod  
    def encrypt_password(password):
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=15))
        print(password_hash)
        return password_hash
    
    @staticmethod
    def username_checker(username):
        login_details_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'account_logins.json')
        login_details_data = json.openJson(login_details_path)

        if len(username) > 0:
            # if username in login_details_data:
            #     return False
            # else:
            #     return True
            return username
        else:
            message = "username should be one character or longer"
            print(message)
    
    @staticmethod
    def password_checker(password, retyped_password):
        if len(password) > 0 and password == retyped_password:
            return password 
        else:
            return None
    @staticmethod   
    def encrypted_password(password):
         return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=15))

