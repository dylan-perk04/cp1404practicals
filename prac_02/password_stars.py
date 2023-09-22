def main():
    password_length = int(input("What is the length of the password: "))
    password = get_password(password_length)
    print_asterisks(password)


def get_password(password_length):
    password = input("What is the password: ")
    while len(password) < password_length:
        print("Password doesn't meet length requirement")
        password = input("What is the password: ")
    return password


def print_asterisks(password):
    print("*" * len(password))


main()
