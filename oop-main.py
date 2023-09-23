import json

class ToDoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []
        return tasks

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task_description):
        self.tasks.append({"task": task_description, "done": False})

    def mark_task_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["done"] = True

    def display_tasks(self):
        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i + 1}. {task['task']} ({status})")

def main():
    filename = "todo.json"
    todo_list = ToDoList(filename)

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_description = input("Enter task description: ")
            todo_list.add_task(task_description)
            todo_list.save_tasks()
            print("Task added successfully!")

        elif choice == "2":
            todo_list.display_tasks()
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            todo_list.mark_task_done(task_index)
            todo_list.save_tasks()
            print("Task marked as done!")

        elif choice == "3":
            todo_list.display_tasks()

        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
