# app/controllers/task_controller.py
from fastapi import APIRouter
from typing import Dict
from services.task_service import TaskService
from Schema.task_schema import Task

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: str):
    return TaskService.get_task(task_id)

@router.post("/{task_id}/cancel", response_model=Dict)
def cancel_task(task_id: str):
    return TaskService.cancel_task(task_id)
