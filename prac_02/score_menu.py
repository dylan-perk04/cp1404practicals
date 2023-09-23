MENU = "Menu:\n(I)nput score:\n(D)isplay result:\n(S)how stars:\n(Q)uit:"


def main():
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "I":
            score = get_valid_score()
        elif choice == "D":
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
    print("*" * score)


main()
