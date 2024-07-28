def show_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def remove_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to remove: ")) - 1
    if 0 <= task_num < len(tasks):
        removed_task = tasks.pop(task_num)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task number.")

tasks = []

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task(tasks)
    elif choice == '2':
        view_tasks(tasks)
    elif choice == '3':
        remove_task(tasks)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
