import logging
import json
from typing import List

from fastapi import APIRouter
from ..models.todo import Todo, TodoUpdate, TodoInDb
from ..service.todo import TodoService

logging.basicConfig(level=logging.INFO)

router = APIRouter()


@router.post("/")
def create_todo(todo: Todo) -> TodoInDb:
    todo_service: TodoService = TodoService()
    return todo_service.create_todo(todo)


@router.get("/")
def list_todo() -> List[TodoInDb]:
    todo_service: TodoService = TodoService()
    return todo_service.read_todos()


@router.get("/{todo_id}")
def get_todo(todo_id: int)->TodoInDb:
    todo_service: TodoService = TodoService()
    return todo_service.read_todo(todo_id=todo_id)


@router.put("/{todo_id}")
def update_todo(todo_id: int, update_data: TodoUpdate)->TodoInDb:
    todo_service: TodoService = TodoService()
    return todo_service.update_todo(todo_id=todo_id, update_data=update_data)


@router.delete("/{todo_id}")
def delete_todo(todo_id: int) -> dict:
    todo_service: TodoService = TodoService()
    todo_service.delete_todo(todo_id=todo_id)
    return {"details": "Todo Delete Successfully."}
