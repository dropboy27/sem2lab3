from datetime import datetime
from src.exceptions.task_exceptions import TaskError


class ShortDescription:
    '''Получение краткого описания (10 символов), Non data дескриптор'''
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        full = obj.description
        if len(full) > 10:
            return full[:10]
        return full

class ReadOnlyInt:
    def __set_name__(self, owner, name):
        self.name = name
        self.private = '_' + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.private)

    def __set__(self, obj, value):
        if self.private in obj.__dict__:
            raise TaskError(f"{self.name} нельзя менять (read-only)")
        if not isinstance(value, int):
            raise TaskError(f"{self.name} должен быть int")
        if value <= 0:
            raise TaskError(f"{self.name} должен быть положительным")
        obj.__dict__[self.private] = value


class ReadOnlyString:
    def __set_name__(self, owner, name):
        self.name = name
        self.private = '_' + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.private)

    def __set__(self, obj, value):
        if self.private in obj.__dict__:
            raise TaskError(f"{self.name} нельзя менять (read-only)")
        if not isinstance(value, str):
            raise TaskError(f"{self.name} должен быть строкой")
        if not value.strip():
            raise TaskError(f"{self.name} не может быть пустым")
        obj.__dict__[self.private] = value

class StatusField:
    def __set_name__(self, owner, name):
        self.name = name
        self.private = '_' + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.private)

    def __set__(self, obj, value):
        allowed = ('новая', 'в работе', 'завершена')
        if value not in allowed:
            raise TaskError(f"Статус должен быть одним из {allowed}")
        obj.__dict__[self.private] = value

class PriorityField:
    def __set_name__(self, owner, name):
        self.name = name
        self.private = '_' + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.private)

    def __set__(self, obj, value):
        if self.private in obj.__dict__:
            raise TaskError("Приоритет нельзя менять (read-only)")
        if not isinstance(value, int):
            raise TaskError("Приоритет должен быть int")
        if not 1 <= value <= 5:
            raise TaskError("Приоритет должен быть от 1 до 5")
        obj.__dict__[self.private] = value

class Task:
    id = ReadOnlyInt()
    priority = PriorityField()
    description = ReadOnlyString()
    status = StatusField()
    short_desc = ShortDescription()

    def __init__(self, id: int, description: str, priority: int, status: str):
        self.id = id
        self.description = description
        self.priority = priority
        self.status = status
        self._created_at = datetime.now()

    @property
    def created_at(self):
        """Только чтение."""
        return self._created_at

    @property
    def is_active(self):
        """Вычисляемое свойство: задача активна, если не завершена."""
        return self.status != 'завершена'

    def __repr__(self):
        return f"Task(id={self.id}, desc='{self.description}', prio={self.priority}, status='{self.status}', created at={self.created_at})"
