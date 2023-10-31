import logging
import json
from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from google.protobuf.json_format import MessageToJson
from starlette.responses import JSONResponse

from ..models.todo import Todo, TodoInDb
from ..service.todo import TodoService

logging.basicConfig(level=logging.INFO)

router = APIRouter()


@router.post("/")
def create_todo(todo: Todo) -> TodoInDb:
    todo_service: TodoService = TodoService()
    return todo_service.add_todo(todo)

@router.get("/")
def list_todo() -> List[TodoInDb]:
    todo_service: TodoService = TodoService()
    return todo_service.read_todos()

@router.get("/{id}")
def get_todo(id:int):
    todo_service: TodoService = TodoService()
    return todo_service.read_todo(id=id)

#
# @router.put("/{id}")
# def update_todo():
#     ...
#
#
# @router.delete("/{id}")
# def delete_todo():
#     ...
