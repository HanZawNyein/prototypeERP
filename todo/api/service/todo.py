import logging
from typing import List

import json
from google.protobuf.json_format import MessageToDict, MessageToJson

from ..repository.todo import TodoRepository
from ..models.todo import Todo, TodoInDb


class TodoService:
    repo: TodoRepository = TodoRepository()

    def add_todo(self, todo: Todo) -> TodoInDb:
        return self.repo.create_todo(todo)
        # return TodoInDb(**json.loads(MessageToJson(Todo(**self.repo.create_todo(todo)))))

    def read_todos(self):
        return self.repo.read_todos()

    def read_todo(self,id:int):
        return self.repo.read_todos()
