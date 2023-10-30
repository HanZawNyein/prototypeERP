- Generate A Proto Code
```zsh
python -m grpc_tools.protoc -I./protos --python_out=./grpc --pyi_out=./todo_grpc --grpc_python_out=./todo_grpc ./protos/todo.proto
```