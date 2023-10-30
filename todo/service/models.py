from sqlalchemy import Column, Integer, String, Boolean

from db import Base


# Define the Todo model
class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    done = Column(Boolean)
