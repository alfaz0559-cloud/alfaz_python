# task_manager_v5.py
# Version 5: Tasks are objects, not dictionaries.

import json


TASKS_FILE = "tasks.json"


class Task:
    """Represents a single task with a description and status."""

    def __init__(self, description, status="pending"):
        """Create a new Task and validate its data."""

        if description.strip() == "":
            raise ValueError("Task description cannot be empty.")

        if status not in ["pending", "completed"]:
            raise ValueError("Task status must be 'pending' or 'completed'.")

        self.description = description
        self.status = status

    def __str__(self):
        """Return a readable string representation of the task."""
        return f"{self.description} [{self.status}]"

    def mark_complete(self):
        """Mark this task as completed."""
        self.status = "completed"

    def is_complete(self):
        """Return True if the task is completed, otherwise False."""
        return self.status == "completed"

    def to_dict(self):
        """Convert the Task object to a dictionary for JSON serialization."""
        return {
            "description": self.description,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task object from a dictionary."""
        return cls(data["description"], data["status"])


def is_empty(tasks):
    """Return True if the task list is empty, otherwise False."""
    return len(tasks) == 0


def load_tasks(filename):
    """Load tasks from a JSON file, returning a list of Task objects."""

    try:
        with open(filename, "r") as f:
            tasks_data = json.load(f)

        tasks = [Task.from_dict(data) for data in tasks_data]

        print(f"Loaded {len(tasks)} task(s) from {filename}.")

        return tasks

    except FileNotFoundError:
        print("No save file found. Starting with an empty task list.")
        return []

    except json.JSONDecodeError:
        print("Save file is corrupted. Starting with an empty task list.")
        return []

    except (KeyError, ValueError) as e:
        print(f"Invalid task data in save file: {e}")
        print("Starting with an empty task list.")
        return []


def save_tasks(tasks, filename):
    """Save a list of Task objects to a JSON file."""

    tasks_data = [task.to_dict() for task in tasks]

    try:
        with open(filename, "w") as f:
            json.dump(tasks_data, f, indent=4)

        print(f"Saved {len(tasks)} task(s).")

    except IOError as e:
        print(f"Error saving tasks: {e}")


def display_tasks(tasks):
    """Display all tasks with their index and status."""

    if is_empty(tasks):
        print("Your task list is empty.")
        return

    print("\n--- Your Tasks ---")

    for index, task in enumerate(tasks):
        print(f" {index + 1}. {task}")

    print("------------------")


def add_task(tasks):
    """Ask the user for a description and add a new Task."""

    description = input("Enter the task description: ")

    try:
        task = Task(description)
        tasks.append(task)

        print(f'Added: "{description}"')

    except ValueError as e:
        print(e)


def mark_task_complete(tasks):
    """Show tasks and keep asking until the user enters a valid task number."""

    if is_empty(tasks):
        print("No tasks to mark.")
        return

    display_tasks(tasks)

    while True:
        task_number = input("Enter the task number to mark complete: ")

        if task_number.isdigit():
            task_index = int(task_number) - 1

            if 0 <= task_index < len(tasks):
                break

        print("Invalid task number. Please try again.")

    task = tasks[task_index]

    if task.is_complete():
        print("That task is already completed.")
    else:
        task.mark_complete()
        print(f'Marked "{task.description}" as completed.')


def delete_task(tasks):
    """Show tasks and keep asking until the user enters a valid task number."""

    if is_empty(tasks):
        print("No tasks to delete.")
        return

    display_tasks(tasks)

    while True:
        task_number = input("Enter the task number to delete: ")

        if task_number.isdigit():
            task_index = int(task_number) - 1

            if 0 <= task_index < len(tasks):
                break

        print("Invalid task number. Please try again.")

    deleted_task = tasks.pop(task_index)

    print(f'Deleted: "{deleted_task.description}"')


def search_tasks(tasks):
    """Return a list of tasks whose descriptions contain the search term."""

    if is_empty(tasks):
        print("Your task list is empty.")
        return []

    search_term = input("Enter a search term: ").strip().lower()

    results = []

    for task in tasks:
        if search_term in task.description.lower():
            results.append(task)

    return results


def display_search_results(results):
    """Display the results returned by search_tasks()."""

    if len(results) == 0:
        print("No tasks found.")
        return

    print("\n--- Search Results ---")

    for index, task in enumerate(results):
        print(f" {index + 1}. {task}")

    print("----------------------")


def main():
    """Run the Task Manager."""

    tasks = load_tasks(TASKS_FILE)

    print("=== Task Manager ===\n")

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Exit")
        print("5. Delete a task")
        print("6. Search tasks")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            add_task(tasks)
            save_tasks(tasks, TASKS_FILE)

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            mark_task_complete(tasks)
            save_tasks(tasks, TASKS_FILE)

        elif choice == "4":
            save_tasks(tasks, TASKS_FILE)
            print("Goodbye!")
            break

        elif choice == "5":
            delete_task(tasks)
            save_tasks(tasks, TASKS_FILE)

        elif choice == "6":
            results = search_tasks(tasks)
            display_search_results(results)

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")


main()