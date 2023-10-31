from typing import Optional
from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: str
    done: bool = False


class Todo(TodoBase):
    ...


class TodoInDb(TodoBase):
    id: int


class TodoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    done: Optional[bool]
