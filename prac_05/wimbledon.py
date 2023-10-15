"""
CP1404 Practical
Program to read, process and display Wimbledon data
Estimated: 50 minutes
Actual: 47 minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Read csv file and print details about Wimbledon champions and countries."""
    records = get_records(FILENAME)
    champion_to_wins, countries = process_records(records)
    display_results(champion_to_wins, countries)


def get_records(filename):
    """Get records from file in list of lists form."""
    records = []
    with open(filename, 'r', encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Create dictionary of champions and a set of countries from records using the list of lists."""
    champion_to_wins = {}
    countries = set()

    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_wins[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_wins[record[CHAMPION_INDEX]] = 1
    return champion_to_wins, countries


def display_results(champion_to_wins, countries):
    """Display champions and countries."""
    print("Wimbledon Champions: ")

    for name, count in champion_to_wins.items():
        print(name, count)

    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
