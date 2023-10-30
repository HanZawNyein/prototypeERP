from db import SessionLocal
import logging
from todo_grpc import todo_pb2_grpc, todo_pb2
from models import Todo

import grpc
from google.protobuf import empty_pb2


# Define the gRPC service
class TodoServicer(todo_pb2_grpc.TodoServiceServicer):

    # Create a new Todo
    def Create(self, request, context):

        todo = Todo(
            title=request.title,
            description=request.description,
            done=request.done
        )
        db = SessionLocal()
        db.add(todo)
        db.commit()
        db.refresh(todo)
        db.close()
        logging.info(f"Todo Created Service.{todo.id}")
        return todo_pb2.Todo(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            done=todo.done
        )

    # Read an existing Todo
    def Read(self, request, context):
        db = SessionLocal()
        todo = db.query(Todo).filter(Todo.id == request.id).first()
        db.close()
        if todo:
            return todo_pb2.Todo(
                id=todo.id,
                title=todo.title,
                description=todo.description,
                done=todo.done
            )
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Todo not found")
            return todo_pb2.Todo()

    # Update an existing Todo
    def Update(self, request, context):
        db = SessionLocal()
        todo = db.query(Todo).filter(Todo.id == request.id).first()
        if todo:
            todo.title = request.title
            todo.description = request.description
            todo.done = request.done
            db.add(todo)
            db.commit()
            db.refresh(todo)
            db.close()
            return todo_pb2.Todo(
                id=todo.id,
                title=todo.title,
                description=todo.description,
                done=todo.done
            )
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Todo not found")
            return todo_pb2.Todo()

    # Delete an existing Todo
    def Delete(self, request, context):
        db = SessionLocal()
        todo = db.query(Todo).filter(Todo.id == request.id).first()
        if todo:
            db.delete(todo)
            db.commit()
            db.close()
            return empty_pb2.Empty()
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Todo not found")
            return empty_pb2.Empty()

    # List all Todos
    def List(self, request, context):
        db = SessionLocal()
        todos = db.query(Todo).all()
        db.close()
        todo_list = [todo_pb2.Todo(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            done=todo.done
        ) for todo in todos]
        logging.info("list todo")
        return todo_pb2.TodoListResponse(todos=todo_list)
