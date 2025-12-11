import json
import os

FILE = "expenses.json"

# Create a file if it doesn't exist
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)


# Load expenses
def load_expenses():
    with open(FILE, "r") as f:
        return json.load(f)


# Save expenses
def save_expenses(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# Add new expense
def add_expense():
    expenses = load_expenses()

    amount = float(input("Enter Amount: "))
    category = input("Enter Category (Food, Travel, Shopping, etc.): ")
    note = input("Enter Note/Description: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


# View all expenses
def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n------ Your Expenses ------")
    for e in expenses:
        print(f"₹{e['amount']} - {e['category']} ({e['note']})")
    print("---------------------------")


# Calculate total spent
def total_spent():
    expenses = load_expenses()
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal Money Spent: ₹{total}")


# Main menu
def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Money Spent")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spent()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again!")


if __name__ == "__main__":
    main()
