# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntodo.proto\x12\x04todo\x1a\x1bgoogle/protobuf/empty.proto\"D\n\x04Todo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04\x64one\x18\x04 \x01(\x08\"-\n\x10TodoListResponse\x12\x19\n\x05todos\x18\x01 \x03(\x0b\x32\n.todo.Todo\"K\n\x0bTodoRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04\x64one\x18\x04 \x01(\x08\x32\xfd\x01\n\x0bTodoService\x12)\n\x06\x43reate\x12\x11.todo.TodoRequest\x1a\n.todo.Todo\"\x00\x12\'\n\x04Read\x12\x11.todo.TodoRequest\x1a\n.todo.Todo\"\x00\x12)\n\x06Update\x12\x11.todo.TodoRequest\x1a\n.todo.Todo\"\x00\x12\x35\n\x06\x44\x65lete\x12\x11.todo.TodoRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x38\n\x04List\x12\x16.google.protobuf.Empty\x1a\x16.todo.TodoListResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'todo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TODO']._serialized_start=49
  _globals['_TODO']._serialized_end=117
  _globals['_TODOLISTRESPONSE']._serialized_start=119
  _globals['_TODOLISTRESPONSE']._serialized_end=164
  _globals['_TODOREQUEST']._serialized_start=166
  _globals['_TODOREQUEST']._serialized_end=241
  _globals['_TODOSERVICE']._serialized_start=244
  _globals['_TODOSERVICE']._serialized_end=497
# @@protoc_insertion_point(module_scope)
