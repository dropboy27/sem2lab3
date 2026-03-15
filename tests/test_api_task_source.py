import time
from unittest.mock import patch
from src.TaskSources.api_task import ApiTaskSource
from src.classes.task_dataclass import Task

def test_api_task_source_default_count():
    source = ApiTaskSource()
    tasks = source.get_tasks()
    assert len(tasks) == 3
    assert all(isinstance(t, Task) for t in tasks)

def test_api_task_source_specific_count():
    source = ApiTaskSource(tasks_count=5)
    tasks = source.get_tasks()
    assert len(tasks) == 5

def test_api_task_source_id_type():
    source = ApiTaskSource(tasks_count=1)
    tasks = source.get_tasks()
    assert isinstance(tasks[0].id, int)
    assert 1000 <= tasks[0].id <= 9999

def test_api_task_source_fields_valid():
    source = ApiTaskSource(10)
    tasks = source.get_tasks()
    possible_descs = ["Process data", "Generate report", "Send email", "Backup database", "Update cache"]
    allowed_statuses = ('новая', 'в работе', 'завершена')
    for task in tasks:
        assert task.description in possible_descs
        assert 1 <= task.priority <= 5
        assert task.status in allowed_statuses

def test_api_task_source_simulate_delay():
    source = ApiTaskSource(simulate_delay=True)
    start = time.time()
    source.get_tasks()
    elapsed = time.time() - start
    assert elapsed >= 0.5

@patch("time.sleep")
def test_api_task_source_delay_disabled(mock_sleep):
    source = ApiTaskSource(simulate_delay=False)
    source.get_tasks()
    mock_sleep.assert_not_called()