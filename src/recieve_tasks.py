from src.classes.task_source_protocol import TaskSource
from src.classes.task_dataclass import Task
def receive(source: TaskSource) -> list[Task]:
    if not isinstance(source, TaskSource):
        raise TypeError(
            f"Объект не реализует протокол TaskSource.")

    tasks = source.get_tasks()
    return tasks
