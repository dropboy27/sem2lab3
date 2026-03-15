from src.classes.task_source_protocol import TaskSource
from src.classes.task_dataclass import Task

class GoodSource:
    def get_tasks(self) -> list[Task]:
        return [Task(id=1, description="test", priority=1, status="новая")]

class BadSource:
    pass

def test_protocol_runtime_checkable():
    assert isinstance(GoodSource(), TaskSource)
    assert not isinstance(BadSource(), TaskSource)