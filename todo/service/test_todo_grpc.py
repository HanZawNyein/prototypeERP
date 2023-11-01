import unittest

import grpc
import main
from todo.service.servicer import TodoServicer
from todo_grpc import todo_pb2, todo_pb2_grpc
from google.protobuf.json_format import MessageToDict

from unittest.mock import Mock


class TestTodoGrpc(unittest.TestCase):
    def setUp(self):
        # Create an instance of your service
        self.servicer = TodoServicer()

        # Create a mock server
        self.server = Mock()
        todo_pb2_grpc.add_TodoServiceServicer_to_server(self.servicer, self.server)

    def test_create_task(self):
        # Define a task to create
        new_task = todo_pb2.Todo(id=1, title="Test Task", description="This is a test task")

        # Mock the gRPC context
        context = Mock()

        # Call the gRPC method
        response = self.servicer.Create(new_task, context)
        response_dict = MessageToDict(response)
        # Verify the response
        self.assertEqual(type(response_dict), dict)


if __name__ == '__main__':
    unittest.main()
