from password_storing import PasswordAccess
 
def main():
    password_manager = PasswordAccess()
 
    answer = input("Are you storing, searching or deleting a password? or do you want to view all passwords?")
 
    if answer == "storing":
        password = input("Enter your password: ")
        password_manager.write_password(password)
    elif answer == "view":
        password_manager.view_passwords()
    elif answer == "searching":
        password = input("Enter Password to search for: ")
        password_manager.search_passwords(password)
    elif answer  == "deleting":
        password = input("Enter the password you wish to delete: ")
        password_manager.delete_entry(password)
    else:
        print("Invalid option. Please choose storing, searching or deleting")
 
if __name__ == "__main__":
    main()