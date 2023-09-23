import json

# Function to load tasks from a JSON file
def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to a JSON file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(tasks, task_description):
    tasks.append({"task": task_description, "done": False})

# Function to mark a task as done
def mark_task_done(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True

# Function to display tasks
def display_tasks(tasks):
    print("\nTo-Do List:")
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i + 1}. {task['task']} ({status})")

# Main function
def main():
    filename = "todo.json"
    tasks = load_tasks(filename)

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_description = input("Enter task description: ")
            add_task(tasks, task_description)
            save_tasks(filename, tasks)
            print("Task added successfully!")

        elif choice == "2":
            display_tasks(tasks)
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            mark_task_done(tasks, task_index)
            save_tasks(filename, tasks)
            print("Task marked as done!")

        elif choice == "3":
            display_tasks(tasks)

        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
