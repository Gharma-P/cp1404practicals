"""
Write a program that stores users email(unique keys) and names(values) in a dictionary.
Ask the user for an email until they enter a blank one
Estimate: 60mins
Actual: 70mins
"""


def main():
    name_to_email = {}
    get_email = input("Enter you email: ").lower()
    while get_email != "":
        name = get_name_from_email(get_email)
        confirmation = input(f"Is your name {name}? (y/n): ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name:")
        name_to_email[get_email] = name
        get_email = input("Email: ")
    for email, name in name_to_email.items():
        print(f"{name}: {email}")


def get_name_from_email(email):
    "Getting name from email"
    name_in_email = email.split("@")[0]
    parts = name_in_email.split('.')
    name = ".".join(parts).title()
    return name


main()
