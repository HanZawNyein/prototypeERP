import logging

import grpc
from fastapi import HTTPException

from .todo_grpc import todo_pb2_grpc
from .todo_grpc import todo_pb2

from ..models.todo import Todo

# Create a gRPC channel and stub
channel = grpc.insecure_channel("localhost:50051")
stub = todo_pb2_grpc.TodoServiceStub(channel)


class TodoRepository:
    def create_todo(self, todo: Todo):
        return stub.Create(todo_pb2.TodoRequest(title=todo.title, description=todo.description))

    def read_todos(self):
        # Read all Todos using the gRPC stub
        response = stub.List(todo_pb2.TodoListResponse())
        logging.info("read todos.")
        logging.info(response)
        return response

    def read_todo(self, todo_id: int):
        # Read a Todo by ID using the gRPC stub
        try:
            response = stub.Read(todo_pb2.TodoRequest(id=todo_id))
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise HTTPException(status_code=404, detail='Todo not found')

