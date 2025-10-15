# app/controllers/project_controller.py
from fastapi import APIRouter
from typing import List, Dict
from services.project_service import ProjectService
from Schema.project_schema import Project

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/", response_model=List[Project])
def get_projects():
    return ProjectService.get_all_projects()

@router.post("/", response_model=Project)
def create_project(payload: Project):
    return ProjectService.create_project(payload.dict())

@router.get("/recent", response_model=List[Project])
def get_recent_projects():
    return ProjectService.get_recent_projects()

@router.get("/{project_id_or_key}", response_model=Project)
def get_project(project_id_or_key: str):
    return ProjectService.get_project_by_id(project_id_or_key)

@router.put("/{project_id_or_key}", response_model=Project)
def update_project(project_id_or_key: str, payload: Project):
    return ProjectService.update_project(project_id_or_key, payload.dict())

@router.delete("/{project_id_or_key}", response_model=Dict)
def delete_project(project_id_or_key: str):
    return ProjectService.delete_project(project_id_or_key)

@router.get("/{project_id_or_key}/statuses", response_model=List[Dict])
def get_project_statuses(project_id_or_key: str):
    return ProjectService.get_project_statuses(project_id_or_key)

@router.get("/{project_id}/hierarchy", response_model=Dict)
def get_project_hierarchy(project_id: str):
    return ProjectService.get_project_hierarchy(project_id)

@router.get("/{project_id_or_key}/notificationscheme", response_model=Dict)
def get_project_notification_scheme(project_id_or_key: str):
    return ProjectService.get_project_notification_scheme(project_id_or_key)
