"""
CP1404 Practical
Program to turn a  data file into lists
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display neatly formatted."""
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)
        print(repr(line))
        line = line.strip()
        parts = line.split(',')
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        print("----------")
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(data):
    """Display subject details by subject, lecturer and number of students."""
    for datum in data:
        print(f"{datum[0]} is taught by {datum[1]} and has {datum[2]} students")


main()
