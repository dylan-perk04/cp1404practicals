"""
CP1404 Practical - Code to test Guitar class code.
Estimation: 10 minutes
Actual: 11 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Demo test code to show how to use Guitar class."""
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    my_spare_guitar = Guitar("Another Guitar", 2013, 10000)

    print(f"{my_guitar.name} get_age() test - Expected 101. Got {my_guitar.get_age()}")
    print(f"{my_spare_guitar.name} get_age() test - Expected 10. Got {my_spare_guitar.get_age()}")
    print(f"{my_guitar.name} is_vintage() test - Expected True. Got {my_guitar.is_vintage()}")
    print(f"{my_spare_guitar.name} is_vintage() test - Expected False. Got {my_spare_guitar.is_vintage()}")


main()
