from password_storing import PasswordAccess

def main():
    password_manager = PasswordAccess()
    
    answer = input("Are you storing or searching or deleting for a password?")
    
    if answer == "storing":
        password = input("Enter your password: ")
        password_manager.write_password(password)
    if answer == "searching":
        password = input("Enter Password to search for: ")
        password_manager.search_passwords(password)
    if answer  == "deleting":
        password = input("Enter the password you wish to delete: ")
        password_manager.delete_entry(password)
    
if __name__ == "__main__":
    main()