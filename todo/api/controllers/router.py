import logging
import json
from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from google.protobuf.json_format import MessageToJson

from ..models.todo import Todo
from ..service.todo import TodoService

logging.basicConfig(level=logging.INFO)

router = APIRouter()


@router.post("/")
def create_todo(todo: Todo):
    todo_service: TodoService = TodoService()
    return todo_service.add_todo(todo)


@router.get("/")
def list_todo()->List[Todo]:
    logging.info("Helo list")
    todo_service: TodoService = TodoService()
    response = todo_service.read_todos()
    logging.info("Fuclk")
    logging.info(response)
    return JSONResponse(content=json.loads(MessageToJson(response))) #todo_service.read_todos()
    ...


@router.get("/{id}")
def get_todo():
    ...


@router.put("/{id}")
def update_todo():
    ...


@router.delete("/{id}")
def delete_todo():
    ...
