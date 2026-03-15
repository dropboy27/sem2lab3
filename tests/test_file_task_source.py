import pytest
from unittest.mock import mock_open, patch
from src.TaskSources.file_task import FileTaskSource
from src.exceptions.file_task_source_exceptions import FileTaskSourceNotFound
from src.classes.task_dataclass import Task

def test_file_task_source_reads_valid_lines():
    mock_content = "1 task1 3 новая\n2 task2 5 в работе\n3 task3 1 завершена\n"
    with patch("builtins.open", mock_open(read_data=mock_content)):
        source = FileTaskSource("tasks.txt")
        tasks = source.get_tasks()
        assert len(tasks) == 3
        assert tasks[0].id == 1
        assert tasks[0].description == "task1"
        assert tasks[0].priority == 3
        assert tasks[0].status == "новая"
        assert tasks[1].id == 2
        assert tasks[2].id == 3

def test_file_task_source_ignores_malformed_lines():
    mock_content = "1 task1 3 новая\nbadline\n2 task2 5\n3 task3 1 завершена extra\n"
    with patch("builtins.open", mock_open(read_data=mock_content)):
        source = FileTaskSource("tasks.txt")
        tasks = source.get_tasks()
        assert len(tasks) == 1
        assert tasks[0].id == 1

def test_file_task_source_empty_file():
    with patch("builtins.open", mock_open(read_data="")):
        source = FileTaskSource("empty.txt")
        tasks = source.get_tasks()
        assert tasks == []

def test_file_task_source_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        source = FileTaskSource("missing.txt")
        with pytest.raises(FileTaskSourceNotFound) as exc_info:
            source.get_tasks()
        assert "missing.txt" in str(exc_info.value)