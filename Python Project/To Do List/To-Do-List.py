tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks found.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                deleted_task = tasks.pop(index)
                print(f"Task '{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input.")
    else:
        print("No tasks found.")

def main():
    while True:
        print("\n===== TODO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using the Todo List!")

if __name__ == "__main__":
    main()
