from random import randint, choice
from src.classes.task_dataclass import Task


class TaskGenerator:
    """Генератор случайных задач."""

    possible_tasks = ('Do homework', 'Make dinner',
                      'Make lunch', 'Make breakfast')

    def __init__(self, tasks_number: int = 1):
        """Инициализация с количеством генерируемых задач."""
        self.tasks_number = tasks_number

    def get_tasks(self) -> list[Task]:
        """Генерирует и возвращает список случайных задач."""
        tasks = []
        for i in range(self.tasks_number):
            tasks.append(Task(id=randint(1, self.tasks_number*10),
                        description=choice(self.possible_tasks), 
                        priority=randint(1,5), 
                        status=choice(['новая', 'в работе', 'завершена'])))
        return tasks