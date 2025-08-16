import json
import os

FILE_NAME = "todo.json"

# Load data from JSON file
def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("⚠️ Error: JSON file is corrupted or empty.")
            return [] 
    return []

# Save data to JSON file
def save_tasks():
    try:
        with open(FILE_NAME, 'w') as file:
            json.dump(To_Do_List, file, indent=4) 
    except Exception as e:
        print(f"⚠️ Error saving tasks: {e}")

# Initialize To_Do_List from file
To_Do_List = load_tasks()

def show_menu():
    print("\n--- TO-DO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    new_id = To_Do_List[-1]['id'] + 1 if To_Do_List else 1
    task = {
        "id": new_id,
        "title": title,
        "description": description
    }
    To_Do_List.append(task)
    save_tasks()
    print("✅ Task added successfully!")

def view_tasks():
    if not To_Do_List:
        print("📭 No tasks found.")
        return
    for task in To_Do_List:
        print(f"\n🆔 ID: {task['id']}")
        print(f"📌 Title: {task['title']}")
        print(f"📝 Description: {task['description']}")

def update_task():
    try:
        task_id = int(input("Enter task ID to update: "))
        for task in To_Do_List:
            if task['id'] == task_id:
                new_title = input("Enter new title: ")
                new_description = input("Enter new description: ")
                task['title'] = new_title
                task['description'] = new_description
                save_tasks()
                print("✏️ Task updated successfully!")
                return
        print("❌ Task not found!")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def delete_task():
    try:
        task_id = int(input("Enter task ID to delete: "))
        for task in To_Do_List:
            if task['id'] == task_id:
                To_Do_List.remove(task)
                save_tasks()
                print("🗑️ Task deleted successfully!")
                return
        print("❌ Task not found!")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Main Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("👋 Exiting the app. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice. Please try again.")


































































