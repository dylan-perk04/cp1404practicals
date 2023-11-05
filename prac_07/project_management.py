"""
CP1404 Practical - Code to test and use Project Class code.
Time Estimation: 13 hours
Actual: 9 hours
"""

import datetime
import os
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
    """Program to load and save a data file and use a list of Project objects."""
    projects = []
    load_file(FILENAME, projects)

    menu_choice = input(MENU_PROMPT).upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = get_valid_filename("Enter filename to load projects from: ")
            load_file(filename, projects)  # Safe to ignore warning
        elif menu_choice == "S":
            filename = get_valid_filename("Enter filename to save projects to: ")
            save_file(filename, projects)
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            date = input("Show projects that start after date (dd/mm/yy): ")
            filtered_projects = filter_projects(projects, date)
            for project in filtered_projects:
                print(project)
        elif menu_choice == "A":
            print("Let's add a new project")
            name = get_valid_text("Name: ")
            start_date = get_valid_date("Start date (dd/mm/yy): ")
            priority = get_valid_integer("Priority: ")
            cost_estimate = get_valid_cost("Cost estimate: $")
            completion_percentage = get_valid_integer("Percent complete: ")
            add_project(projects, name, start_date, priority, cost_estimate, completion_percentage)
        elif menu_choice == "U":
            for i, project in enumerate(projects):
                print(f"{i} {project.__str__()}")
            project_number = get_valid_project_number(projects, "Project choice: ")
            update_project(projects, project_number)
        else:
            print("Invalid menu choice")
        menu_choice = input(MENU_PROMPT).upper()


def load_file(filename, projects):
    """Load projects from a data file."""
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
    """Display incomplete and completed projects sorted by priority."""
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
    """Sort projects by inputted date."""
    formatted_date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > formatted_date]
    filtered_projects.sort(key=lambda project: project.start_date)
    return filtered_projects


def add_project(projects, name, start_date, priority, cost_estimate, completion_percentage):
    """Add a new project's detail to list of projects."""
    project_to_add = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project_to_add)


def update_project(projects, project_number):
    """Modify completion percentage and/or priority."""
    project = projects[project_number]
    new_percentage = input("New Percentage: ")
    if new_percentage:
        project.update_completion(int(new_percentage))
    new_priority = input("New Priority: ")
    if new_priority:
        project.update_priority(int(new_priority))


def save_file(filename, projects):
    """Save projects to data file."""
    with open(filename, 'w') as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            project_data = [
                project.name, project.start_date.strftime("%d/%m/%Y"), str(project.priority),
                f"{project.cost_estimate:.1f}", str(project.completion_percentage)]
            print('\t'.join(project_data), file=out_file)


def get_valid_text(prompt):
    """Get a valid name for a new project."""
    text = input(prompt)
    # Text input can't be blank
    while text == "":
        print("Input can not be blank.")
        text = input(prompt)
    return text


def get_valid_integer(prompt):
    """Get a valid integer."""
    # Run the loop until a valid year is inputted
    is_valid_integer = False
    while not is_valid_integer:
        try:
            integer = int(input(prompt))
            is_valid_integer = True
        except ValueError:
            print("Invalid input; enter a valid number.")
    return integer  # Safe to ignore warning


def get_valid_cost(prompt):
    """Get a valid cost estimate for a new project."""
    # Run the loop until a valid year is inputted
    is_valid_cost = False
    while not is_valid_cost:
        try:
            cost = float(input(prompt))
            is_valid_cost = True
        except ValueError:
            print("Invalid input; enter a valid number.")
    return cost  # Safe to ignore warning


def get_valid_date(prompt):
    """Get a valid date for a new project."""
    is_valid_date = False
    while not is_valid_date:
        try:
            date = input(prompt)
            start_date = datetime.datetime.strptime(date, "%d/%m/%y").date()
            is_valid_date = True
        except ValueError:
            print("Invalid date. Please use (dd/mm/yy) format.")
    return start_date  # Safe to ignore warning


def get_valid_filename(prompt):
    """Get a valid filename to load from or save to."""
    is_valid_filename = False
    while not is_valid_filename:
        try:
            filename = input(prompt)
            if os.path.isfile(filename):
                is_valid_filename = True
        except FileNotFoundError:
            print("File not found.")
    return filename  # Safe to ignore warning


def get_valid_project_number(projects, prompt):
    """Get a valid project number to update."""
    is_valid_project_number = False
    while not is_valid_project_number:
        try:
            project_number = int(input(prompt))
            if 0 <= project_number < len(projects):
                is_valid_project_number = True
        except ValueError:
            print("Invalid project choice.")
    return project_number  # Safe to ignore warning


main()
