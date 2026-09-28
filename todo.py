tasks = []

while True:
    print("\n1.Add Task 2.View Tasks 3.Mark Complete 4.Delete Task 5.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
    elif choice == '2':
        for i, t in enumerate(tasks):
            status = "✔" if t["done"] else "✘"
            print(f"{i+1}. {t['task']} [{status}]")
    elif choice == '3':
        idx = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
    elif choice == '4':
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
    elif choice == '5':
        break
    else:
        print("Invalid choice")
