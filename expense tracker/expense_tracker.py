import json
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    amount = float(input("Enter expense amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully.")


def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n=== EXPENSES ===")

    for expense in expenses:
        print("--------------------")
        print("Amount:", expense["amount"])
        print("Category:", expense["category"])
        print("Date:", expense["date"])


def calculate_totals(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    print("\n=== TOTALS BY CATEGORY ===")

    if not totals:
        print("No expenses recorded.")
        return

    for category, total in totals.items():
        print(f"{category}: {total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add expense")
        print("2. Display expenses")
        print("3. Calculate totals by category")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            display_expenses(expenses)

        elif choice == "3":
            calculate_totals(expenses)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
