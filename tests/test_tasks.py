import pytest
from app import create_task, list_tasks, update_task, delete_task

def test_create_task():
    task = create_task("Estudar Kanban", "Alta")
    assert task["title"] == "Estudar Kanban"

def test_list_tasks():
    assert isinstance(list_tasks(), list)

def test_update_task():
    task = create_task("Testar sistema", "Média")
    updated = update_task(task["id"], new_status="Concluído")
    assert updated["status"] == "Concluído"

def test_delete_task():
    task = create_task("Remover tarefa", "Baixa")
    assert delete_task(task["id"]) is True

def test_create_task_without_title():
    with pytest.raises(ValueError):
        create_task("", "Alta")
