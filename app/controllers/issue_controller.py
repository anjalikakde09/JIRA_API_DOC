# app/controllers/issue_controller.py
from fastapi import APIRouter
from typing import List, Dict, Any
from services.issue_service import IssueService
from Schema.issue_schema import Issue, BulkIssueUpdate, BulkFetchRequest, IssueAssigneeUpdate, IssueNotifyPayload

router = APIRouter(prefix="/issues", tags=["Issues"])

@router.post("/changelog/bulkfetch", response_model=List[Issue])
def bulk_fetch(payload: BulkFetchRequest):
    return IssueService.bulk_fetch(payload.dict())

@router.get("/events", response_model=List[Dict])
def get_events():
    return IssueService.get_events()

@router.post("/", response_model=Issue)
def create_issue(payload: Dict[str, Any]):
    return IssueService.create_issue(payload)

@router.post("/bulk", response_model=Dict)
def bulk_update(payload: BulkIssueUpdate):
    return IssueService.bulk_issue_update(payload.dict())

@router.post("/bulkfetch", response_model=Dict)
def bulk_fetch_issues(payload: Dict[str, Any]):
    return IssueService.bulk_fetch_issues(payload)

@router.get("/{issue_id_or_key}", response_model=Issue)
def get_issue(issue_id_or_key: str):
    return IssueService.get_issue(issue_id_or_key)

@router.put("/{issue_id_or_key}", response_model=Issue)
def update_issue(issue_id_or_key: str, payload: Dict[str, Any]):
    return IssueService.update_issue(issue_id_or_key, payload)

@router.delete("/{issue_id_or_key}", response_model=Dict)
def delete_issue(issue_id_or_key: str):
    return IssueService.delete_issue(issue_id_or_key)

@router.put("/{issue_id_or_key}/assignee", response_model=Dict)
def update_assignee(issue_id_or_key: str, payload: IssueAssigneeUpdate):
    return IssueService.update_assignee(issue_id_or_key, payload.dict())

@router.post("/{issue_id_or_key}/notify", response_model=Dict)
def notify_issue(issue_id_or_key: str, payload: IssueNotifyPayload):
    return IssueService.notify_issue(issue_id_or_key, payload.dict())
