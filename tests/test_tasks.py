import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import TaskManager
import pytest


def test_add_task():
    manager = TaskManager()
    manager.add_task("Estudar Python", "Alta")
    assert len(manager.tasks) == 1


def test_add_task_empty_title():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task("", "Baixa")


def test_update_task():
    manager = TaskManager()
    manager.add_task("Tarefa", "Média")
    manager.update_task(0, completed=True)
    assert manager.tasks[0].completed is True


def test_remove_task():
    manager = TaskManager()
    manager.add_task("Excluir", "Baixa")
    manager.remove_task(0)
    assert len(manager.tasks) == 0

