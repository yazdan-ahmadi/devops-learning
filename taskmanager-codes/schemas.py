
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    completed: bool | None = None

class Task(TaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True
