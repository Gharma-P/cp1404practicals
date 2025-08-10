"""
This program handles user interaction through a menu driven loop
"""
from project import Project
from datetime import datetime

FILE_NAME = "projects.txt"


def load_projects_from_file(filename):
    projects = []
    try:
        with open(filename, "r") as file:
            file.readline()
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) < 5:
                    continue
                name = parts[0]
                start_date = parts[1]
                priority = parts[2]
                cost_estimate = parts[3]
                completion = parts[4]
                project = Project(name, start_date, priority, cost_estimate, completion)
                projects.append(project)
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print("File not found")
    return projects


def save_projects_to_file(projects, filename):
    # filename = input("Enter filename to save projects to:")
    try:
        with open(filename, "w") as file:
            file.write("Name\tStart Date\tPriority\tCost\tCompletion\n")

            for project in projects:
                line = f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate:.2f}\t{project.completion}\n"
                file.write(line)

        print(f"{len(projects)} projects saved to {filename}")

    except OSError:
        print("Error saving")


def display_projects(projects):
    incomplete = [p for p in projects if p.completion < 100]
    complete = [p for p in projects if p.completion == 100]

    incomplete.sort(key=lambda p: p.priority, reverse=True)
    complete.sort(key=lambda p: p.priority, reverse=True)

    print("\nIncomplete projects:")
    for project in incomplete:
        print(f" {project}")

    print("\nComplete projects:")
    for project in complete:
        print(f" {project}")


def filter_projects_by_date(projects):
    date_str = input("Show projects that start on or after date (YYYY-MM-DD):")
    try:
        filter_date = datetime.strptime(date_str, "%Y-%m-%d.").date()

    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD")
        return

    filtered = [p for p in projects if datetime.strptime(p.start_date, "%Y-%m-%d") == filter_date]
    filtered.sort(key=lambda p: datetime.strptime(p.start_date, "%Y-%m-%d").date())

    print(f"\nProjects starting on of after {filter_date}:")
    for projects in filtered:
        print(f" {projects}")


def add_new_project(projects):
    print("\nNew project:")
    name = input("Name:").strip()
    start_date = get_valid_date("Start date (YYYY-MM-DD):")
    priority = get_valid_int("Priority: (eg. 1 for high priority): ")
    cost_estimate = get_valid_float("Cost estimate ($): ")
    completion = get_valid_int("Completion percentage (0-100):", 0, 100)
    new_project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(new_project)
    print("\nProject added")


def get_valid_date(prompt):
    date_str = input(prompt).strip()
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD")
        return get_valid_date(prompt)


def get_valid_int(prompt, min_value=None, max_value=None):
    try:
        value = int(input(prompt).strip())
        if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
            print(f"Value must be between {min_value} and {max_value}.")
            return get_valid_int(prompt, min_value, max_value)
        return value
    except ValueError:
        print("Invalid integer value.")
        return get_valid_int(prompt, min_value, max_value)


def get_valid_float(prompt):
    try:
        return float(input(prompt).strip())
    except ValueError:
        return get_valid_float(prompt)


def update_project(projects):
    if not projects:
        print("No projects to update")
        return

    print("Projects:")
    for i, project in enumerate(projects):
        print(f" {i}  - {project}")

    try:
        index = int(input("Enter the number of a project to update: ").strip())
        project = projects[index]
    except  (ValueError, IndexError):
        print("Invalid section")
        return

    print(f"Updating: {project}")

    new_priority = input(f"New priority (leave blank to keep {project.priority}):").strip()
    if new_priority != "":
        try:
            project.priority = int(new_priority)
        except ValueError:
            print("Invalid input")

    new_completion = input(f"New completion % (leave blank to keep {project.completion}):").strip()
    if new_completion != "":
        try:
            completion = int(new_completion)
            if 0 <= completion <= 100:
                project.completion = completion
            else:
                print("Invalid input must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Not updated")
    print("Project updated")


def main():
    """Read a text file and sort"""
    projects = []
    print("Welcome to Pythonic Project Management")
    choice = ""
    while choice != "q":
        print("Menu:")
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").strip().lower()

        if choice == "l":
            filename = "projects.txt"
            projects = load_projects_from_file(filename)

        elif choice == "s":
            filename = input("Filename to save: ").strip()
            save_projects_to_file(projects, filename)

        elif choice == "d":
            display_projects(projects)

        elif choice == "f":
            filter_projects_by_date(projects)

        elif choice == "a":
            add_new_project(projects)

        elif choice == "u":
            update_project(projects)

        elif choice == "q":
            save = input("Would you like to save projects.txt? (y/n)").strip
            if save == "y":
                filename = input("Filename to save: ").strip()
                save_projects_to_file(projects, filename)
            print("Thankyou for using custom built project management software")

        else:
            print("Invalid input")


main()
