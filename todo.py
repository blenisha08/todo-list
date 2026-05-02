tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
        else:
            print("Invalid number")

    elif choice == "4":
        break

    else:
        print("Invalid choice")