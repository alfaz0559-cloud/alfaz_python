# task_manager_v6.py
# Module 6: The TaskManager
# Includes all Module 6 exercises.

import json
from datetime import datetime


class Task:
    """Represents a single task."""

    def __init__(
        self,
        description,
        status="pending",
        priority="medium",
        due_date=None
    ):
        self.description = description
        self.status = status
        self.priority = priority
        self.due_date = due_date

    def __str__(self):
        parts = [f"{self.description} [{self.status}]"]
        parts.append(f"priority: {self.priority}")

        if self.due_date:
            parts.append(f"due: {self.due_date}")

        return " | ".join(parts)

    def mark_complete(self):
        """Mark this task as completed."""
        self.status = "completed"

    def is_complete(self):
        """Return True if the task is completed."""
        return self.status == "completed"

    def to_dict(self):
        """Convert the task to a dictionary for JSON serialization."""
        return {
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "due_date": self.due_date,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task from a dictionary."""
        return cls(
            description=data["description"],
            status=data.get("status", "pending"),
            priority=data.get("priority", "medium"),
            due_date=data.get("due_date"),
        )


class DeadlineTask(Task):
    """
    A specialized Task that always has a due date
    and always starts with high priority.
    """

    def __init__(self, description, due_date):
        super().__init__(
            description,
            priority="high",
            due_date=due_date
        )


class TaskManager:
    """Manages a collection of tasks."""

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self._load_tasks()

    # -------------------------------------------------
    # Internal persistence methods
    # -------------------------------------------------

    def _load_tasks(self):
        """Load tasks from the JSON file into self.tasks."""

        try:
            with open(self.filename, "r") as f:
                tasks_data = json.load(f)

            self.tasks = [Task.from_dict(d) for d in tasks_data]

            print(
                f"Loaded {len(self.tasks)} task(s) "
                f"from {self.filename}."
            )

        except FileNotFoundError:
            print(
                f"No save file found for {self.filename}. "
                "Starting with an empty task list."
            )
            self.tasks = []

        except json.JSONDecodeError:
            print(
                f"{self.filename} is corrupted. "
                "Starting with an empty task list."
            )
            self.tasks = []

    def _save_tasks(self):
        """Save self.tasks to the JSON file."""

        tasks_data = [task.to_dict() for task in self.tasks]

        try:
            with open(self.filename, "w") as f:
                json.dump(tasks_data, f, indent=4)

        except IOError as e:
            print(f"Error saving tasks: {e}")

    # -------------------------------------------------
    # Exercise 1: View pending tasks
    # -------------------------------------------------

    def view_pending(self):
        """Display only tasks that are still pending."""

        pending_tasks = [
            task for task in self.tasks
            if task.status == "pending"
        ]

        if len(pending_tasks) == 0:
            print("There are no pending tasks.")
            return

        print("\n--- Pending Tasks ---")

        for index, task in enumerate(pending_tasks):
            print(f" {index + 1}. {task}")

        print("---------------------")

    # -------------------------------------------------
    # Exercise 2: Sort tasks by priority
    # -------------------------------------------------

    def view_by_priority(self):
        """
        Display tasks sorted by priority:
        high, medium, low.
        """

        if len(self.tasks) == 0:
            print("Your task list is empty.")
            return

        priority_order = {
            "high": 0,
            "medium": 1,
            "low": 2
        }

        sorted_tasks = sorted(
            self.tasks,
            key=lambda task: priority_order.get(
                task.priority,
                1
            )
        )

        print("\n--- Tasks by Priority ---")

        for index, task in enumerate(sorted_tasks):
            print(f" {index + 1}. {task}")

        print("-------------------------")

    # -------------------------------------------------
    # Add task
    # -------------------------------------------------

    def add_task(self):
        """Interactively add a new task."""

        description = input("Enter the task description: ")

        if not description.strip():
            print("Task description cannot be empty.")
            return

        priority = input(
            "Priority (high/medium/low) [medium]: "
        ).strip().lower()

        if priority not in ("high", "medium", "low"):
            print("Invalid priority. Using medium.")
            priority = "medium"

        due_date = input(
            "Due date (YYYY-MM-DD) or press Enter for none: "
        ).strip()

        if due_date == "":
            due_date = None

        task = Task(
            description,
            priority=priority,
            due_date=due_date
        )

        self.tasks.append(task)
        self._save_tasks()

        print(f'Added: "{description}"')

    # -------------------------------------------------
    # View all tasks
    # -------------------------------------------------

    def view_tasks(self):
        """Display all tasks."""

        if len(self.tasks) == 0:
            print("Your task list is empty.")
            return

        print("\n--- Your Tasks ---")

        for index, task in enumerate(self.tasks):
            print(f" {index + 1}. {task}")

        print("------------------")

    # -------------------------------------------------
    # Mark task complete
    # -------------------------------------------------

    def mark_task_complete(self):
        """Show tasks and let the user mark one as complete."""

        if len(self.tasks) == 0:
            print("No tasks to mark.")
            return

        self.view_tasks()

        while True:
            task_number_str = input(
                "Enter the task number to mark complete: "
            )

            if not task_number_str.isdigit():
                print("Please enter a valid number.")
                continue

            task_index = int(task_number_str) - 1

            if 0 <= task_index < len(self.tasks):
                break

            print("Invalid task number. Please try again.")

        task = self.tasks[task_index]

        if task.is_complete():
            print("That task is already completed.")
        else:
            task.mark_complete()
            self._save_tasks()

            print(
                f'Marked "{task.description}" as completed.'
            )

    # -------------------------------------------------
    # Delete task
    # -------------------------------------------------

    def delete_task(self):
        """Show tasks and let the user delete one."""

        if len(self.tasks) == 0:
            print("No tasks to delete.")
            return

        self.view_tasks()

        while True:
            task_number_str = input(
                "Enter the task number to delete: "
            )

            if not task_number_str.isdigit():
                print("Please enter a valid number.")
                continue

            task_index = int(task_number_str) - 1

            if 0 <= task_index < len(self.tasks):
                break

            print("Invalid task number. Please try again.")

        removed = self.tasks.pop(task_index)

        self._save_tasks()

        print(f'Deleted: "{removed.description}"')

    # -------------------------------------------------
    # Exercise 4: Add a DeadlineTask
    # -------------------------------------------------

    def add_deadline_task(self):
        """Add a DeadlineTask with high priority."""

        description = input(
            "Enter the deadline task description: "
        )

        if not description.strip():
            print("Task description cannot be empty.")
            return

        due_date = input(
            "Enter the due date (YYYY-MM-DD): "
        ).strip()

        if not due_date:
            print("A deadline is required.")
            return

        task = DeadlineTask(
            description,
            due_date
        )

        self.tasks.append(task)
        self._save_tasks()

        print(
            f'Added deadline task: "{description}" '
            f"(high priority, due {due_date})"
        )

    # -------------------------------------------------
    # Run the program
    # -------------------------------------------------

    def run(self):
        """Run the interactive Task Manager."""

        print("=== Task Manager ===")
        print(f"Using file: {self.filename}")

        while True:
            print("\nWhat would you like to do?")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Mark a task as complete")
            print("4. Delete a task")
            print("5. View pending tasks")
            print("6. View tasks by priority")
            print("7. Add a deadline task")
            print("8. Exit")

            choice = input("\nEnter your choice (1-8): ")

            if choice == "1":
                self.add_task()

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                self.mark_task_complete()

            elif choice == "4":
                self.delete_task()

            elif choice == "5":
                self.view_pending()

            elif choice == "6":
                self.view_by_priority()

            elif choice == "7":
                self.add_deadline_task()

            elif choice == "8":
                self._save_tasks()
                print("Goodbye!")
                break

            else:
                print(
                    "Invalid choice. "
                    "Please enter a number from 1 to 8."
                )


# -------------------------------------------------
# Exercise 3: Multiple Task Managers
# -------------------------------------------------

def choose_manager():
    """
    Create two TaskManager objects and let the user
    choose between the work and personal task lists.
    """

    work_manager = TaskManager("work.json")
    personal_manager = TaskManager("personal.json")

    while True:
        print("\n=== Task Manager Selection ===")
        print("1. Work tasks")
        print("2. Personal tasks")
        print("3. Exit")

        choice = input(
            "\nWhich task list would you like to use? "
        )

        if choice == "1":
            work_manager.run()

        elif choice == "2":
            personal_manager.run()

        elif choice == "3":
            work_manager._save_tasks()
            personal_manager._save_tasks()

            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# -------------------------------------------------
# Program entry point
# -------------------------------------------------

if __name__ == "__main__":
    choose_manager()
