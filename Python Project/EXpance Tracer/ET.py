import datetime

def add_expense(expense_list):
    title = input("Enter the expense title: ")
    amount = float(input("Enter the expense amount: "))
    date = input("Enter the date (format: dd-mm-yyyy): ")
    category = input("Enter the expense category: ")
    expense = {
        "title": title,
        "amount": amount,
        "date": date,
        "category": category
    }
    expense_list.append(expense)
    print("Expense added successfully!")

def view_expenses(expense_list):
    if expense_list:
        print("Expenses:")
        for index, expense in enumerate(expense_list, start=1):
            print(f"{index}. Title: {expense['title']}, Amount: {expense['amount']}, Date: {expense['date']}, Category: {expense['category']}")
    else:
        print("No expenses found.")

def delete_expense(expense_list):
    view_expenses(expense_list)
    if expense_list:
        try:
            index = int(input("Enter the expense number to delete: ")) - 1
            if 0 <= index < len(expense_list):
                deleted_expense = expense_list.pop(index)
                print("Expense deleted successfully!")
                print(f"Deleted Expense: Title: {deleted_expense['title']}, Amount: {deleted_expense['amount']}, Date: {deleted_expense['date']}, Category: {deleted_expense['category']}")
            else:
                print("Invalid expense number.")
        except ValueError:
            print("Invalid input.")
    else:
        print("No expenses found.")

def main():
    expenses = []
    
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using the Expense Tracker!")

if __name__ == "__main__":
    main()
