import logging
from typing import List

from fastapi.exceptions import HTTPException

import grpc
from google.protobuf.json_format import MessageToDict

from .todo_grpc import todo_pb2_grpc
from .todo_grpc import todo_pb2

from ...service.todo_grpc.todo_pb2 import TodoRequest, TodoListResponse, Todo


class TodoRepository:
    # Create a gRPC channel and stub
    channel = grpc.insecure_channel("localhost:50051")
    stub = todo_pb2_grpc.TodoServiceStub(channel)

    def create_todo(self, title, description, done) -> Todo:
        response = self.stub.Create(todo_pb2.TodoRequest(title=title, description=description, done=done))
        return response

    def read_todos(self) -> TodoListResponse:
        return self.stub.List(todo_pb2.TodoListResponse())

    def read_todo(self, todo_id: int) -> Todo:
        try:
            return self.stub.Read(TodoRequest(id=todo_id))
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise HTTPException(status_code=404, detail='Todo not found')

    #
    def update_todo(self, todo_id: int, **kwargs) -> Todo:
        try:
            self.stub.Read(TodoRequest(id=todo_id))
            request = TodoRequest(id=todo_id, **kwargs)
            # Update the Todo using the gRPC stub
            response = self.stub.Update(request)
            return response
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise HTTPException(status_code=404, detail='Todo not found')
