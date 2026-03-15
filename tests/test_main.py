import pytest
from unittest.mock import patch
from src.main import main
from src.classes.task_dataclass import Task

def test_main_non_numeric_input(capsys):
    """Ввод не числа в меню."""
    inputs = ['abc', '5']
    with patch('builtins.input', side_effect=inputs):
        main()
    captured = capsys.readouterr()
    assert 'введите число' in captured.out.lower()

def test_main_show_tasks_no_tasks(capsys):
    """Пункт 4, когда задач нет."""
    inputs = ['4', '5']
    with patch('builtins.input', side_effect=inputs):
        main()
    captured = capsys.readouterr()
    assert 'нет задач' in captured.out.lower()

def test_main_show_tasks_invalid_choice(capsys):
    """Пункт 4 с неверным выбором формата."""
    inputs = ['2', '1', '4', '3', '5']
    with patch('builtins.input', side_effect=inputs):
        main()
    captured = capsys.readouterr()
    assert 'неверный выбор' in captured.out.lower()