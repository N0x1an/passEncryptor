import csv
from rich import print
from password_encryption import Encryption

class PasswordAccess:
    encryption_manager = Encryption()
    
    def __init__(self):
        hashed_password = None
    
    def search_passwords(self, password):
        with open('passwords.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == password:
                    print("[green]Password found! [blue]" + row[1])
                    return True
            return False
        
    def write_password(self, password):
        hashed_password = self.encryption_manager.hash_password(password)
        in_csv = self.check_existing(password)
        if in_csv is True:
            print ("Password already encrypted")
            return
        else:
            with open('passwords.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([password, hashed_password.decode('utf-8')])
                print("[green]Password saved! [blue]" + hashed_password.decode('utf-8') )
            
    def check_existing(self, password):
        with open('passwords.csv', 'r', newline='') as csvfile:
            reader =  csv.reader(csvfile)
            for row in reader:
                if row[0] == password:
                    return True
        return False
    
    def delete_entry(self, password):
        in_csv = self.check_existing(password)
        if in_csv is True:
            with open('passwords.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                data = list(reader)
                for i, row in enumerate(data):
                    if row[0] == password:
                        del data[i]
                        break
            with open('passwords.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)
                print("[green]Password deleted!")
        
        