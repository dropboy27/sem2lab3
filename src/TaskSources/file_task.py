from src.classes.task_dataclass import Task
from src.exceptions.file_task_source_exceptions import FileTaskSourceNotFound
from src.exceptions.task_exceptions import TaskError

class FileTaskSource:
    """Источник задач из текстового файла."""
    def __init__(self, filename: str):
        self.filename = filename
    def get_tasks(self) -> list[Task]:
        tasks = []
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(maxsplit=3)
                    if len(parts) == 4:
                        try:
                            id_part, desc, priority_str, status = parts
                            try:
                                id_val = int(id_part)
                            except ValueError:
                                id_val = id_part
                            priority = int(priority_str)
                            task = Task(
                                id=id_val,
                                description=desc,
                                priority=priority,
                                status=status
                            )
                            tasks.append(task)
                        except (ValueError, TaskError) as e:
                            print(f"Ошибка в строке '{line}': {e}")
        except FileNotFoundError as e:
            raise FileTaskSourceNotFound(self.filename) from e
        return tasks