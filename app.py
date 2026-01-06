class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority):
        if not title:
            raise ValueError("Título não pode ser vazio")
        task = Task(title, priority)
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def update_task(self, index, title=None, priority=None, completed=None):
        task = self.tasks[index]
        if title:
            task.title = title
        if priority:
            task.priority = priority
        if completed is not None:
            task.completed = completed

    def remove_task(self, index):
        self.tasks.pop(index)
