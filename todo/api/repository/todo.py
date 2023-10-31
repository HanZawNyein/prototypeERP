import logging
from typing import List

import grpc
from google.protobuf.json_format import MessageToJson, MessageToDict

from .todo_grpc import todo_pb2_grpc
from .todo_grpc import todo_pb2

from ..models.todo import Todo, TodoInDb

# Create a gRPC channel and stub
channel = grpc.insecure_channel("localhost:50051")
stub = todo_pb2_grpc.TodoServiceStub(channel)


class TodoRepository:
    def create_todo(self, todo: Todo) -> TodoInDb:
        response = stub.Create(todo_pb2.TodoRequest(title=todo.title, description=todo.description, done=todo.done))
        return TodoInDb(**MessageToDict(response))

    def read_todos(self) -> List[TodoInDb]:
        # Read all Todos using the gRPC stub
        response = stub.List(todo_pb2.TodoListResponse())

        response_dict = MessageToDict(response).get('todos')
        logging.info(response_dict)
        todos = [TodoInDb(**todo) for todo in response_dict]
        logging.info(todos)
        return todos
