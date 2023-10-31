from typing import List

from google.protobuf.json_format import MessageToDict

from ..repository.todo import TodoRepository
from ..models.todo import Todo, TodoInDb, TodoUpdate


class TodoService:
    repo: TodoRepository = TodoRepository()

    def create_todo(self, todo: Todo) -> TodoInDb:
        return TodoInDb(**MessageToDict(self.repo.create_todo(**todo.model_dump(exclude_unset=True))))

    def read_todos(self) -> List[TodoInDb]:
        return [TodoInDb(**todo) for todo in MessageToDict(self.repo.read_todos()).get('todos')]

    def read_todo(self, todo_id: int) -> TodoInDb:
        return TodoInDb(**MessageToDict(self.repo.read_todo(todo_id=todo_id)))

    def update_todo(self, todo_id: int, update_data: TodoUpdate) -> TodoInDb:
        return TodoInDb(**MessageToDict(self.repo.update_todo(todo_id=todo_id,**update_data.model_dump(exclude_unset=True))))
