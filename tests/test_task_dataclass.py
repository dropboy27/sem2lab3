import pytest
from datetime import datetime
from src.classes.task_dataclass import Task, TaskError

class TestTask:
    def test_create_valid_task(self):
        t = Task(id=1, description="Do homework", priority=3, status="новая")
        assert t.id == 1
        assert t.description == "Do homework"
        assert t.priority == 3
        assert t.status == "новая"
        assert isinstance(t.created_at, datetime)
        assert t.is_active is True
        
    def test_create_task_with_invalid_id_type(self):
        with pytest.raises(TaskError, match="id должен быть int"):
            Task(id=3.14, description="x", priority=1, status="новая")
        with pytest.raises(TaskError, match="id должен быть int"):
            Task(id="123", description="x", priority=1, status="новая")

    def test_create_task_with_negative_id(self):
        with pytest.raises(TaskError, match="id должен быть положительным"):
            Task(id=-5, description="x", priority=1, status="новая")

    def test_create_task_with_invalid_priority_type(self):
        with pytest.raises(TaskError, match="Приоритет должен быть int"):
            Task(id=1, description="x", priority="3", status="новая")

    def test_create_task_with_priority_out_of_range(self):
        with pytest.raises(TaskError, match="Приоритет должен быть от 1 до 5"):
            Task(id=1, description="x", priority=6, status="новая")
        with pytest.raises(TaskError, match="Приоритет должен быть от 1 до 5"):
            Task(id=1, description="x", priority=0, status="новая")

    def test_create_task_with_invalid_description_type(self):
        with pytest.raises(TaskError, match="description должен быть строкой"):
            Task(id=1, description=123, priority=1, status="новая")

    def test_create_task_with_empty_description(self):
        with pytest.raises(TaskError, match="description не может быть пустым"):
            Task(id=1, description="   ", priority=1, status="новая")

    def test_create_task_with_invalid_status(self):
        with pytest.raises(TaskError, match="Статус должен быть одним из"):
            Task(id=1, description="x", priority=1, status="готово")

    def test_readonly_fields_cannot_be_changed(self):
        t = Task(id=1, description="test", priority=2, status="новая")
        with pytest.raises(TaskError, match="id нельзя менять"):
            t.id = 10
        with pytest.raises(TaskError, match="Приоритет нельзя менять"):
            t.priority = 5
        with pytest.raises(TaskError, match="description нельзя менять"):
            t.description = "new"
        with pytest.raises(AttributeError):
            t.created_at = datetime.now()

    def test_status_can_be_changed(self):
        t = Task(id=1, description="test", priority=2, status="новая")
        t.status = "в работе"
        assert t.status == "в работе"
        t.status = "завершена"
        assert t.is_active is False

    def test_property_is_active(self):
        t = Task(id=1, description="test", priority=2, status="новая")
        assert t.is_active is True
        t.status = "завершена"
        assert t.is_active is False

    def test_short_description_non_data_descriptor(self):
        t = Task(id=1, description="очень длинное описание задачи", priority=2, status="новая")
        assert t.short_desc == "очень длин"
        t.short_desc = "произвольная строка"
        assert t.short_desc == "произвольная строка"
        del t.short_desc
        assert t.short_desc == "очень длин"

    def test_short_description_shorter_than_10(self):
        t = Task(id=1, description="коротко", priority=2, status="новая")
        assert t.short_desc == "коротко"

    def test_repr_contains_fields(self):
        t = Task(id=42, description="test", priority=3, status="новая")
        repr_str = repr(t)
        assert "id=42" in repr_str
        assert "desc='test'" in repr_str
        assert "prio=3" in repr_str
        assert "status='новая'" in repr_str
        assert "created at=" in repr_str