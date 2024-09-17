"""
CP1404 - Practical
Get a password and display asterisks
"""


def main():
    """Program to get valid password and print asterisks using functions."""
    password_length = int(input("What is the length of the password: "))
    password = get_valid_password(password_length)
    print_asterisks(password)


def get_valid_password(password_length):
    """Get valid password."""
    password = input("What is the password: ")
    while len(password) < password_length:
        print("Password doesn't meet length requirement")
        password = input("What is the password: ")
    return password


def print_asterisks(password):
    """Print asterisks the length of the password."""
    print("*" * len(password))


main()
