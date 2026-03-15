from src.TaskSources.task_generator import TaskGenerator
from src.classes.task_dataclass import Task

def test_task_generator_default_count():
    gen = TaskGenerator()
    tasks = gen.get_tasks()
    assert len(tasks) == 1
    assert isinstance(tasks[0], Task)

def test_task_generator_specific_count():
    gen = TaskGenerator(tasks_number=5)
    tasks = gen.get_tasks()
    assert len(tasks) == 5

def test_task_generator_ids_within_range():
    n = 3
    gen = TaskGenerator(tasks_number=n)
    tasks = gen.get_tasks()
    for task in tasks:
        assert 1 <= task.id <= n * 10

def test_task_generator_priority_in_range():
    gen = TaskGenerator(10)
    tasks = gen.get_tasks()
    for task in tasks:
        assert 1 <= task.priority <= 5

def test_task_generator_status_valid():
    gen = TaskGenerator(10)
    tasks = gen.get_tasks()
    allowed = ('новая', 'в работе', 'завершена')
    for task in tasks:
        assert task.status in allowed

def test_task_generator_description_from_possible():
    gen = TaskGenerator(10)
    tasks = gen.get_tasks()
    possible = gen.possible_tasks
    for task in tasks:
        assert task.description in possible