from task_manager import TaskManager

manager = TaskManager("tasks.json")

while True:
    print("===== Student Task Tracker =====")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit\n")

    choice = input("Enter choice: ").strip()

    # 1. Add New Task
    if choice == "1":
        title = input("Task Title: ").strip()
        description = input("Task Description: ").strip()

        if not title:
            print("Title cannot be empty. Task was not added.")
        else:
            manager.add_task(title, description)

    # 2. View All Tasks
    elif choice == "2":
        manager.view_tasks()

    # 3. Update an Existing Task
    elif choice == "3":
        if not manager.tasks:
            print("No tasks available to update.")
        else:
            manager.view_tasks()
            try:
                index = int(input("Enter task number to update: ").strip()) - 1

                if 0 <= index < len(manager.tasks):
                    new_title = input("New Title (leave blank to keep same): ").strip()
                    new_description = input("New Description (leave blank to keep same): ").strip()

                    if new_title:
                        manager.tasks[index].title = new_title
                    if new_description:
                        manager.tasks[index].description = new_description

                    print("Task updated successfully!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid numeric value.")

    # 4. Delete a Task
    elif choice == "4":
        if not manager.tasks:
            print("No tasks available to delete.")
        else:
            manager.view_tasks()
            try:
                index = int(input("Enter task number to delete: ").strip()) - 1

                if 0 <= index < len(manager.tasks):
                    task_to_delete = manager.tasks[index]
                    confirm = input(f"Are you sure you want to delete '{task_to_delete.title}'? (y/n): ").lower()

                    if confirm == "y":
                        manager.tasks.pop(index)
                        print("Task deleted successfully!")
                    else:
                        print("Delete cancelled.")

                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid numeric value.")

    # 5. Exit
    elif choice == "5":
        print("Saving tasks... Exiting program.")
        manager.save_to_file()
        break

    # Invalid Option
    else:
        print("Invalid choice. Please select a number from 1 to 5.")

    print()
