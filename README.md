# alfaz_python
python exercises

Module 2 Exercise 3 — List of lists vs dictionaries
List of lists
tasks = [
    ["Buy groceries", "pending"],
    ["Read a book", "completed"],
    ["Walk the dog", "pending"]
]

print(tasks[0][0])
print(tasks[0][1])

The problem is that:

tasks[0][0]

doesn't tell you much.

With dictionaries:

tasks = [
    {
        "description": "Buy groceries",
        "status": "pending"
    },
    {
        "description": "Read a book",
        "status": "completed"
    }
]

print(tasks[0]["description"])
print(tasks[0]["status"])

The second version is much more readable.
