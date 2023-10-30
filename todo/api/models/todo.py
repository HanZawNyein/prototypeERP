from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: str
    done: bool

class Todo(BaseModel):
    ...


class TodoInDb(TodoBase):
    id: int
