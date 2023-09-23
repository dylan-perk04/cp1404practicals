"""
CP1404/CP5632 - Practical
Fixed program to determine score result using function
"""

import random


def main():
    """Program to get a user's numeric score and display its result."""
    score = float(input("Enter score: "))
    result = determine_user_result(score)
    print(f"Your result is {result}")
    random_score = random.randint(0, 100)
    result = determine_user_result(random_score)
    print(f"Your random score is {random_score} and your result is {result}")


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


main()
