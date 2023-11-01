import grpc
import logging
from concurrent import futures

from db import Base, engine
from servicer import TodoServicer
from todo_grpc import todo_pb2_grpc

logging.basicConfig(level=logging.INFO)


def run(insecure_port: int = 50051):
    # Create the table
    Base.metadata.create_all(bind=engine)

    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add the TodoServicer to the server
    todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoServicer(), server)

    # Start the server
    server.add_insecure_port(f'[::]:{insecure_port}')
    server.start()
    logging.info("Server started on port 50051")
    server.wait_for_termination()
    return f"localhost:{insecure_port}", server


if __name__ == '__main__':
    grpc_url, server = run()
    server.start()
    logging.info("Server started on port 50051")
    server.wait_for_termination()