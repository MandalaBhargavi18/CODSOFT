# Define a function to display the menu options
def display_menu():
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

# Define a function to add a task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

# Define a function to view tasks
def view_tasks(tasks):
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index}. {task['task']} - {status}")
    else:
        print("No tasks available.")

# Define a function to mark a task as completed
def mark_completed(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

# Define a function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the index of the task to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted successfully!")
    else:
        print("Invalid task index.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()