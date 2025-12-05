import json
import os
import random
from datetime import datetime
from task import Task

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()

    def generate_unique_id(self):
        existing_ids = {t.task_id for t in self.tasks}
        while True:
            new_id = random.randint(1, 1000)
            if new_id not in existing_ids:
                return new_id

    def add_task(self, title, description):
        try:
            task_id = self.generate_unique_id()
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task = Task(task_id, title.strip(), description.strip(), created_at)
            self.tasks.append(task)
            print(f"Task '{title}' added successfully!")
        except Exception as e:
            print("Failed to add task:", e)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        print("\n===== All Tasks =====")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. Title      : {task.title}")
            print(f"   Description: {task.description}")
            print(f"   Created At : {task.created_at}")
            print("------------------------")
        print()

    def find_task_index_by_id(self, task_id):
        for index, task in enumerate(self.tasks):
            if task.task_id == task_id:
                return index
        return None

    def update_task(self, task_id, new_title=None, new_description=None):
        try:
            index = self.find_task_index_by_id(task_id)
            if index is None:
                print(f"No task found with ID {task_id}.")
                return

            if new_title and new_title.strip():
                self.tasks[index].title = new_title.strip()
            if new_description and new_description.strip():
                self.tasks[index].description = new_description.strip()

            print("Task updated successfully!")
        except Exception as e:
            print("Failed to update task:", e)

    def delete_task(self, task_id):
        try:
            index = self.find_task_index_by_id(task_id)
            if index is None:
                print(f"No task found with ID {task_id}.")
                return

            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task.title}' (ID: {removed_task.task_id}) deleted successfully!")
        except Exception as e:
            print("Failed to delete task:", e)

    def save_to_file(self):
        try:
            data = [task.to_dict() for task in self.tasks]
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print("Failed to save tasks:", e)

    def load_from_file(self):
        if not os.path.exists(self.filename):
            self.tasks = []
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    self.tasks = []
                    return
                data = json.loads(content)
                self.tasks = [Task.from_dict(item) for item in data]
        except FileNotFoundError:
            print("Task file not found. Starting with empty task list.")
            self.tasks = []
        except json.JSONDecodeError:
            print("Error reading tasks file. Starting with empty task list.")
            self.tasks = []
        except Exception as e:
            print("An unexpected error occurred while loading tasks:", e)
            self.tasks = []
