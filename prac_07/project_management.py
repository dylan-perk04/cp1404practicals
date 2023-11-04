"""
Time Estimation: 13 hours
"""

MENU_PROMPT = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
               "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")
FILENAME = "projects.txt"
NAME_INDEX = 0
START_DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_ESTIMATE_INDEX = 3
COMPLETION_PERCENTAGE = 4


def main():
    projects = []
    load_projects(FILENAME, projects)

    menu_choice = input(MENU_PROMPT).upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            # do thing
        elif menu_choice == "S":
            print("Enter details for a new song.")
        elif menu_choice == "D":
            # do thing
        elif menu_choice == "F":
            # do thing
        elif menu_choice == "A":
            # do thing
        elif menu_choice == "U":
            # do thing
        else:
            print("Invalid menu choice")
        menu_choice = input(MENU_PROMPT).upper()
    print(projects)


def load_projects(filename, projects):
    # Load projects from a data file
    with open(filename, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split('\t')
            projects.append(parts)
    return projects


main()
