# todo.py
# Simple Command-Line To-Do List App

tasks = []

def show_tasks():
    """Display all tasks"""
    if not tasks:
        print("\nYour to-do list is empty.\n")
    else:
        print("\nYour to-do list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()  # empty line for readability

def add_task():
    """Add a task to the list"""
    task = input("Enter a task: ")
    tasks.append(task)
    print(f'"{task}" has been added!')

def remove_task():
    """Remove a task by its number"""
    show_tasks()
    if tasks:
        try:
            index = int(input("Enter the task number to remove: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index-1)
                print(f'"{removed}" has been removed!')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main loop of the app"""
    while True:
        print("Options:")
        print("[1] Show tasks")
        print("[2] Add task")
        print("[3] Remove task")
        print("[4] Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
