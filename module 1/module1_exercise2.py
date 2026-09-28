# module1_exercise2.py

tasks = [
    "Learn Python",
    "Practice lists",
    "Learn dictionaries",
    "Build a project",
    "Read documentation"
]

print("First task:", tasks[0])
print("Last task:", tasks[-1])

print("Number of tasks:", len(tasks))

tasks.append("Practice functions")

print("After append:")
print(tasks)

print("New length:", len(tasks))


print(tasks[100])
