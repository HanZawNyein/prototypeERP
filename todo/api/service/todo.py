from typing import List

from ..repository.todo import TodoRepository
from ..models.todo import Todo


class TodoService:
    repo: TodoRepository = TodoRepository()

    def add_todo(self, todo: Todo):
        result = self.repo.create_todo(todo)
        return result

    def read_todos(self):
        return self.repo.read_todos()
