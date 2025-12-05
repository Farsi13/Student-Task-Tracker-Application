from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, created_at):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        return Task(
            task_id=data.get("id"),
            title=data.get("title", ""),
            description=data.get("description", ""),
            created_at=data.get("created_at", "")
        )
