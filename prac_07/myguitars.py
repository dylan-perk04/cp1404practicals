"""
CP1404 Practicql
Code to run Guitar Class
"""

from guitar import Guitar

FILENAME = "guitars.csv"
NAME_INDEX = 0
YEAR_INDEX = 1
COST_INDEX = 2


def main():
    guitars = []
    load_file(guitars)

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added")
        print()
        name = input("Name: ")

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    save_file(guitars)


def load_file(guitars):
    with open(FILENAME, 'r') as out_file:
        for line in out_file:
            parts = line.strip().split(',')
            name = parts[NAME_INDEX]
            year = parts[YEAR_INDEX]
            cost = parts[YEAR_INDEX]
            guitar_to_add = Guitar(name, int(year), float(cost))
            guitars.append(guitar_to_add)


def save_file(guitars):
    with open(FILENAME, 'w') as out_file:
        for guitar in guitars:
            parts = [guitar.name, str(guitar.year), str(guitar.cost)]
            print(','.join(parts), file=out_file)


main()
