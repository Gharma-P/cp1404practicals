"""
User Password Check
"""
password_length = 6
password = input("Enter Password: ")
while len(password) < password_length:
    print("Password too short")
    password = input("Enter Password: ")
print("*" * len(password))



