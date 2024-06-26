import csv
import os
from rich import print
from password_encryption import Encryption

class PasswordAccess:
    encryption_manager = Encryption()

    def __init__(self):
        self.filepath = 'passwords.csv'
        self.create_file_if_not_exists()

    def create_file_if_not_exists(self):
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                # Optionally write a header
                writer.writerow(['Password', 'HashedPassword'])

    def search_passwords(self, password):
        found = "default-value"
        with open(self.filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == password:
                    print("[green]Password found! [blue]" + row[1])
                    found = row[0] + " : " + row[1]
                    return found
            return "Password not found"
        
    def view_passwords(self):
        passwords = []
        with open(self.filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print("[green] " + row[0] + "[blue] " + row[1])
                passwords.append((row[0], row[1]))
            return passwords
            
    def write_password(self, password):
        hashed_password = self.encryption_manager.hash_password(password)
        in_csv = self.check_existing(password)
        if in_csv is True:
            print("Password already encrypted")
            return
        else:
            with open(self.filepath, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([password, hashed_password.decode('utf-8')])
                print("[green]Password saved! [blue]" + hashed_password.decode('utf-8'))

    def check_existing(self, password):
        with open(self.filepath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == password:
                    return True
        return False

    def delete_entry(self, password):
        in_csv = self.check_existing(password)
        if in_csv is True:
            with open(self.filepath, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                data = list(reader)
                for i, row in enumerate(data):
                    if row[0] == password:
                        del data[i]
                        break
            with open(self.filepath, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)
                print("[green]Password deleted!")
