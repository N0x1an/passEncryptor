import bcrypt
from rich import print
 
class Encryption:
    def __init__(self):
        self.salt = None
        self.hashed = None
 
    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed
 
    def check(self, password):
        hashed_password = self.hash_password(password)
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            print ("[green]Password has been hashed properly")
            print(hashed_password)
            return True
        else:
            print ("[red]Password has NOT been hashed properly")
            print(hashed_password)
            return False