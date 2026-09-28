# module2_exercise1.py

tasks = []

print("=== Task Manager ===")

while True:
    print("\nWhat would you like to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        description = input("Enter the task description: ")

        task = {
            "description": description,
            "status": "pending"
        }

        tasks.append(task)

        print(f'Added: "{description}"')

    elif choice == "2":
        if len(tasks) == 0:
            print("Your task list is empty.")
        else:
            print("\n--- Your Tasks ---")

            for index, task in enumerate(tasks):
                print(
                    f"{index + 1}. "
                    f"{task['description']} "
                    f"[{task['status']}]"
                )

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to mark.")
        else:
            for index, task in enumerate(tasks):
                print(
                    f"{index + 1}. "
                    f"{task['description']} "
                    f"[{task['status']}]"
                )

            task_number = input(
                "Enter the task number to mark complete: "
            )

            if task_number.isdigit():
                task_index = int(task_number) - 1

                if 0 <= task_index < len(tasks):
                    tasks[task_index]["status"] = "completed"
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for index, task in enumerate(tasks):
                print(
                    f"{index + 1}. "
                    f"{task['description']} "
                    f"[{task['status']}]"
                )

            task_number = input(
                "Enter the task number to delete: "
            )

            if task_number.isdigit():
                task_index = int(task_number) - 1

                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)

                    print(
                        f'Deleted: "{removed_task["description"]}"'
                    )
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
