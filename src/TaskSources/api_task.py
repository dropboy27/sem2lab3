import time
from random import randint, choice
from src.classes.task_dataclass import Task
from src.classes.task_source_protocol import TaskSource

class ApiTaskSource:
    """
    Простая API-заглушка, имитирующая получение задач из внешнего источника.
    """
    def __init__(self, tasks_count: int = 3, simulate_delay: bool = True):
        """
        :param tasks_count: количество задач, которые вернёт API
        :param simulate_delay: имитировать ли задержку ответа
        """
        self.tasks_count = tasks_count
        self.simulate_delay = simulate_delay

    def get_tasks(self) -> list[Task]:
        """
        Возвращает список задач. Имитирует задержку сетевого запроса.
        """
        if self.simulate_delay:
            time.sleep(0.5 + randint(0, 100) / 100)
        tasks = []
        possible_descriptions = ["Process data", "Generate report", "Send email", "Backup database", "Update cache"]

        for i in range(self.tasks_count):
            task = Task(
                id=randint(1000, 9999),
                description=choice(possible_descriptions),
                priority=randint(1,5),
                status=choice(['новая', 'в работе', 'завершена'])
            )
            tasks.append(task)

        return tasks