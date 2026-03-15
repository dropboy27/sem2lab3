from src.classes.task_dataclass import Task


class TaskQueue:
    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        self._tasks.append(task)

    def __iter__(self):
        for task in self._tasks:
            yield task

    def filter_by_priority(self, priority, condition):
        # print(f"1 - lower than {priority}\n 2 - higher than {priority}\n 3 - equal to {priority}")
        if condition == 1:
            for task in self._tasks:
                if task.priority < priority:
                    yield task
        if condition == 2:
            for task in self._tasks:
                if task.priority > priority:
                    yield task
        if condition == 3:
            for task in self._tasks:
                if task.priority == priority:
                    yield task
        else:
            raise ValueError("condition must be 1, 2 or 3")

    def filter_by_status(self, status, condition):
        # print(f"1 - show all tasks with {status}\n 2 - show all tasks without {status}")
        if condition == 1:
            for task in self._tasks:
                if task.status == status:
                    yield task
        if condition == 2:
            for task in self._tasks:
                if task.status != status:
                    yield task
        else:
            raise ValueError("condition must be 1 or 2")

    def filter_by_id(self, id, condition):
        # print(f"1 - lower than {id}\n 2 - higher than {id}\n 3 - equal to {id}")
        if condition == 1:
            for task in self._tasks:
                if task.id < id:
                    yield task
        if condition == 2:
            for task in self._tasks:
                if task.id > id:
                    yield task
        if condition == 3:
            for task in self._tasks:
                if task.id == id:
                    yield task
        else:
            raise ValueError("condition must be 1, 2 or 3")
