import json
from pathlib import Path

FILE = Path("tasks.json")

try:
    tasks = json.loads(FILE.read_text()) if FILE.exists() else []
except (ValueError, OSError):
    tasks = []

while True:
    print("\n===== TASK MANAGER =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose: ").strip()

    if choice == "1":
        title = input("Enter task: ").strip()
        if title:
            tasks.append({"title": title, "done": False})
            print("Task added!")

    elif choice == "2":
        for i, task in enumerate(tasks, 1):
            status = "DONE" if task["done"] else "PENDING"
            print(f"{i}. {task['title']} [{status}]")

    elif choice in ("3", "4"):
        try:
            number = int(input("Task number: ")) - 1
            if not 0 <= number < len(tasks):
                raise ValueError
        except ValueError:
            print("Invalid task number")
            continue

        if choice == "3":
            tasks[number]["done"] = True
            print("Task completed!")
        else:
            tasks.pop(number)
            print("Task deleted!")

    elif choice == "5":
        break

    else:
        print("Invalid option")
        continue

    FILE.write_text(json.dumps(tasks, indent=2))
