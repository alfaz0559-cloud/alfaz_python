# module1_exercise1.py

tasks = ["Learn Python", "Build a Task Manager"]

print("Before adding:")
print(tasks)

new_task = input("Enter another task: ")
tasks.append(new_task)

print("\nAfter adding:")
print(tasks)
