- Generate A Proto Code
```zsh
python -m grpc_tools.protoc -I./protos --python_out=./grpc --pyi_out=./grpc --grpc_python_out=./grpc ./protos/todo.proto
```