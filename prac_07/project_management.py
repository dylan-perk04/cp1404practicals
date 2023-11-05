"""
Time Estimation: 13 hours
"""

MENU_PROMPT = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
               "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit\n>>> ")
FILENAME = "projects.txt"
NAME_INDEX = 0
START_DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_ESTIMATE_INDEX = 3
COMPLETION_PERCENTAGE = 4


def main():
    projects = []
    load_file(FILENAME, projects)

    menu_choice = input(MENU_PROMPT).upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = input("Enter filename to load projects from: ")
            load_file(filename, projects)
        elif menu_choice == "S":
            filename = input("Enter filename to save projects to: ")
            save_file(filename, projects)
        # elif menu_choice == "D":
        #     # do thing
        # elif menu_choice == "F":
        #     # do thing
        # elif menu_choice == "A":
        #     # do thing
        # elif menu_choice == "U":
        #     # do thing
        else:
            print("Invalid menu choice")
        menu_choice = input(MENU_PROMPT).upper()


def load_file(filename, projects):
    with open(filename, 'r') as in_file:
        in_file.readline()  # Skip the header line
        for line in in_file:
            parts = line.strip().split('\t')
            projects.append(parts)
    return projects


def save_file(filename, projects):
    with open(filename, 'w') as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print('\t'.join(project), file=out_file)


main()
