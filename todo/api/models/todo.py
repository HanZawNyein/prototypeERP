from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: str
    done: bool


class Todo(TodoBase):
    ...


class TodoInDb(TodoBase):
    id: int
