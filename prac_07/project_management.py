"""
Time Estimation: 13 hours
"""

import datetime
from prac_07.project import Project


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
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            date = input("Show projects that start after date (dd/mm/yy): ")
            filtered_projects = filter_projects(projects, date)
            for project in filtered_projects:
                print(project)
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
            name = parts[NAME_INDEX]
            start_date = parts[START_DATE_INDEX]
            priority = int(parts[PRIORITY_INDEX])
            cost_estimate = float(parts[COST_ESTIMATE_INDEX])
            complete_percentage = int(parts[COMPLETION_PERCENTAGE])
            project_to_add = Project(name, start_date, priority, cost_estimate, complete_percentage)
            projects.append(project_to_add)
    return projects


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]

    incomplete_projects.sort(key=lambda project: project.priority)
    completed_projects.sort(key=lambda project: project.priority)

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"    {project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"    {project}")


def filter_projects(projects, date):
    formatted_date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > formatted_date]
    filtered_projects.sort(key=lambda project: project.start_date)
    return filtered_projects

def save_file(filename, projects):
    with open(filename, 'w') as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            project_data = [
                project.name, project.start_date.strftime("%d/%m/%Y"), str(project.priority),
                f"{project.cost_estimate:.1f}", str(project.completion_percentage)]
            print('\t'.join(project_data), file=out_file)


main()
