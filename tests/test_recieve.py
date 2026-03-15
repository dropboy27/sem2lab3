import pytest
from unittest.mock import Mock
from src.recieve_tasks import receive
from src.classes.task_source_protocol import TaskSource
from src.classes.task_dataclass import Task
from src.exceptions.file_task_source_exceptions import FileTaskSourceNotFound

class GoodSource:
    def get_tasks(self) -> list[Task]:
        return [Task(id=1, description="test", priority=1, status="новая")]

class BadSource:
    pass

def test_receive_with_good_source():
    source = GoodSource()
    tasks = receive(source)
    assert len(tasks) == 1
    assert isinstance(tasks[0], Task)

def test_receive_raises_on_non_protocol():
    source = BadSource()
    with pytest.raises(TypeError, match="не реализует протокол TaskSource"):
        receive(source)

def test_receive_passes_through_exceptions():
    class BrokenSource:
        def get_tasks(self):
            raise FileTaskSourceNotFound("test.txt")
    source = BrokenSource()
    with pytest.raises(FileTaskSourceNotFound):
        receive(source)