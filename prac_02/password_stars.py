password_length = int(input("What is the length of the password: "))
password = input("What is the password: ")
while len(password) < password_length:
    print("Password doesn't meet length requirement")
    password = input("What is the password: ")

print("*" * len(password))
