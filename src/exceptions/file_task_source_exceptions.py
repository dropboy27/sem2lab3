class TaskSourceError(Exception):
    pass

class FileTaskSourceNotFound(TaskSourceError):
    def __init__(self, filename: str):
        self.filename = filename
        super().__init__(f"Файл '{filename}' не найден.")

