# app/Schema/project_schema.py
from pydantic import BaseModel
from typing import List, Optional, Dict

class Project(BaseModel):
    id: Optional[str]
    key: Optional[str]
    name: str
    projectTypeKey: Optional[str]
    lead: Optional[Dict]
    description: Optional[str]
    url: Optional[str]
    notificationScheme: Optional[int]
    permissionScheme: Optional[int]
    avatarId: Optional[int]
    categoryId: Optional[int]
    issueSecurityScheme: Optional[int]
    assigneeType: Optional[str]
    projectTemplateKey: Optional[str]

class ProjectsResponse(BaseModel):
    projects: List[Project]
