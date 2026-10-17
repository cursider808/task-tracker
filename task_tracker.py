```python
import sys
import os
import json
from datetime import datetime

TODO_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def add_task(description):
    tasks = load_tasks()
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    now = datetime.now().isoformat()
    
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Task with ID {task_id} not found.")
        return
    save_tasks(new_tasks)
    print(f"Task {task_id} deleted successfully.")

def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}.")
            return
    print(f"Task with ID {task_id} not found.")

def list_tasks(status=None):
    tasks = load_tasks()
    filtered_tasks = [t for t in tasks if status is None or t["status"] == status]
    
    if not filtered_tasks:
        print("No tasks found.")
        return
    
    for t in filtered_tasks:
        print(f"[{t['id']}] {t['description']} - Status: {t['status']} (Created: {t['createdAt']})")

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py <command> [arguments]")
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) > 2:
        add_task(sys.argv[2])
    elif command == "update" and len(sys.argv) > 3:
        update_task(int(sys.argv[2]), sys.argv[3])
    elif command == "delete" and len(sys.argv) > 2:
        delete_task(int(sys.argv[2]))
    elif command == "mark-in-progress" and len(sys.argv) > 2:
        mark_task(int(sys.argv[2]), "in-progress")
    elif command == "mark-done" and len(sys.argv) > 2:
        mark_task(int(sys.argv[2]), "done")
    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)
    else:
        print("Invalid command or missing arguments.")

if __name__ == "__main__":
    main()
```
