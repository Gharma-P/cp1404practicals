"""
User Password Check
"""
def main():

    password_length = 6
    password = get_password(password_length)
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password(password_length):
    password = input("Enter Password: ")
    while len(password) < password_length:
        print("Password too short")
        password = input("Enter Password: ")
    return password


main()



