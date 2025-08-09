
To_Do_List = []

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
    task = {
         "id": len(To_Do_List) + 1,
        "title": title,
        "description": description}
    To_Do_List.append(task)
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
    task_id = int(input("Enter task ID to update: "))
    for task in To_Do_List:
        if task['id'] == task_id:
            new_title = input("Enter new title: ")
            new_description = input("Enter new description: ")
            task['title'] = new_title
            task['description'] = new_description
            print("✏️ Task updated successfully!")
            return
    print("❌ Task not found!")  


def delete_task():
    task_id = int(input("Enter task ID to delete: "))
    for task in To_Do_List:
        if task['id'] == task_id:
            To_Do_List.remove(task)
            print("🗑️ Task deleted successfully!")
            return
    print("❌ Task not found!")

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


































































