from typing import Protocol, runtime_checkable
from src.classes.task_dataclass import Task


@runtime_checkable
class TaskSource(Protocol):
    """Протокол источника задач. Любой объект, реализующий этот протокол,
    должен предоставлять метод get_tasks, возвращающий список задач Task."""
    def get_tasks(self) -> list[Task]:
        """Возвращает список задач из источника."""
        pass
