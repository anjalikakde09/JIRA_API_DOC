# app/Schema/task_schema.py
from pydantic import BaseModel
from typing import Optional, Dict

class Task(BaseModel):
    id: str
    key: Optional[str]
    summary: Optional[str]
    status: Optional[str]
    assignee: Optional[Dict]
    description: Optional[str]
    project: Optional[Dict]

class TaskResponse(BaseModel):
    task: Task
