"""
CP1404 Practical
Program to display expected name from an email using a dictionary
"""


def main():
    """Create and display dictionary of emails_to_names."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        confirmation_prompt = input(f"Is your name {name}? (Y/n) ").lower()

        if confirmation_prompt != "y" and confirmation_prompt != "":
            name = input("Name: ")

        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract expected name from email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = ' '.join(parts).title()
    return name


main()
