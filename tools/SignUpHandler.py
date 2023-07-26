import bcrypt 

class SignnUpHandler:

    @staticmethod  
    def encrypt_password(password):
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=15))
        print(password_hash)
        return password_hash
    
    @staticmethod
    def username_checker(username):
        return len(username) > 0
    
    @staticmethod
    def password_checker(password, retyped_password):
        if len(password) > 0 and password == retyped_password:
            return True 
        else:
            return None
    @staticmethod   
    def encrypted_password(password):
         return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=15))

