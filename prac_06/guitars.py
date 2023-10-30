"""
CP1404 Practical - Code to test Guitar class code.
Estimation: 20 minutes
Actual: 37 minutes
"""
from prac_06.guitar import Guitar


def main():
    """Program to get and display guitar information using Guitar class."""
    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added")
        print()
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    max_guitar_name_length = max(len(guitar.name) for guitar in guitars)

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>{max_guitar_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f}"
              f"{' (vintage)' if guitar.is_vintage() else ''}")


main()
