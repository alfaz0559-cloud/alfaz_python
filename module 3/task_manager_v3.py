# task_manager_v3.py

def is_empty(tasks):
    """Return True if the task list is empty, otherwise return False."""
    return len(tasks) == 0


def display_tasks(tasks):
    """Display all tasks with their index and status."""
    if is_empty(tasks):
        print("Your task list is empty.")
        return

    print("\n--- Your Tasks ---")

    for index, task in enumerate(tasks):
        print(f" {index + 1}. {task['description']} [{task['status']}]")

    print("------------------")


def add_task(tasks):
    """Ask the user for a description and add a new task."""
    description = input("Enter the task description: ")

    if description.strip() == "":
        print("Task description cannot be empty.")
        return

    task = {
        "description": description,
        "status": "pending"
    }

    tasks.append(task)

    print(f'Added: "{description}"')


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

    if tasks[task_index]["status"] == "completed":
        print("That task is already completed.")
    else:
        tasks[task_index]["status"] = "completed"
        print(f'Marked "{tasks[task_index]["description"]}" as completed.')


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

    print(f'Deleted: "{deleted_task["description"]}"')


def search_tasks(tasks):
    """Return a list of tasks whose descriptions contain the search term."""

    search_term = input("Enter a search term: ").strip().lower()

    results = []

    for task in tasks:
        if search_term in task["description"].lower():
            results.append(task)

    return results


def display_search_results(results):
    """Display the results returned by search_tasks()."""

    if len(results) == 0:
        print("No tasks found.")
        return

    print("\n--- Search Results ---")

    for index, task in enumerate(results):
        print(f" {index + 1}. {task['description']} [{task['status']}]")

    print("----------------------")


def main():
    """Run the Task Manager."""

    tasks = []

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

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            mark_task_complete(tasks)

        elif choice == "4":
            print("Goodbye!")
            break

        elif choice == "5":
            delete_task(tasks)

        elif choice == "6":
            results = search_tasks(tasks)
            display_search_results(results)

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")


main()
