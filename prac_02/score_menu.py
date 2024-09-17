"""
CP1404 - Practical
Menu using functions that gets a valid score, prints results and prints as many asterisks as the score
"""

MENU = "Menu:\n(G)et valid score:\n(P)rint result:\n(S)how stars:\n(Q)uit:"


def main():
    """Program to display menu that gets valid score, prints result and prints as many asterisks as the score using
    functions."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_user_result(score)
            print(f"Your score is {score} and your result is {result}")
        elif choice == "S":
            print_asterisks(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    """Get valid score between 0-100."""
    score = int(input("What is your score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = int(input("What is your score: "))
    return score


def determine_user_result(score):
    """Determine the result of user's score."""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Pass"
    else:
        result = "Bad"
    return result


def print_asterisks(score):
    """Print as many asterisks as the score."""
    print("*" * score)


main()
