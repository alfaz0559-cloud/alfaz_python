# task_manager_v1.py
# Version 1: Store tasks in a list, add one, display them all.
tasks = []
print("=== Task Manager ===")
print("Your task list is empty. Let's add some tasks.\n")
first_task = input("Enter your first task: ")
tasks.append(first_task)
second_task = input("Enter your second task: ")
tasks.append(second_task)
third_task = input("Enter your third task: ")
tasks.append(third_task)
print("\nYour tasks:")
print(tasks)
