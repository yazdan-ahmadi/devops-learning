from sqlalchemy import Column, Integer, String, Text, Boolean
from database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True, nullable=False)
    description = Column(Text, nullable=True)
    completed = Column(Boolean, default=False)
