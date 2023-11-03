from guitar import Guitar

FILENAME = "guitars.csv"
NAME_INDEX = 0
YEAR_INDEX = 1
COST_INDEX = 2


def main():
    guitars = []

    with open(FILENAME, 'r') as out_file:
        for line in out_file:
            parts = line.strip().split(',')
            parts[YEAR_INDEX] = int(parts[YEAR_INDEX])
            parts[COST_INDEX] = float(parts[COST_INDEX])
            guitar_to_add = Guitar(parts[NAME_INDEX], parts[YEAR_INDEX], parts[COST_INDEX])
            guitars.append(guitar_to_add)

    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
