# password encryptor
# github link: https://github.com/N0x1an/passEncryptor

# Python program that hashes input passwords

# Python module that encrypts string inputs
import bcrypt

# Hash function of the password
def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    # Store the hashed pasword
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

# Check function to make sure if there is an error in hashing it will be caught and raise an error
def check_password(password, hashed_password):
    # Check if the provided password matches the stored hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# Inputting the password
inputPassword = input("Please input your password: ")

# Hashing the password
hashedPass = hash_password(inputPassword)

# Checking if the hashing properly hashed, if not raise error otherwise print hashed password
if check_password(inputPassword, hashedPass):
    print("password is: ", hashedPass)
else:    
    raise "error, please try again"