# app/Schema/issue_schema.py
from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class IssueFields(BaseModel):
    summary: Optional[str]
    description: Optional[str]
    project: Optional[Dict]
    issuetype: Optional[Dict]
    assignee: Optional[Dict]
    reporter: Optional[Dict]
    labels: Optional[List[str]]
    priority: Optional[Dict]
    fixVersions: Optional[List[Dict]]
    customfield_10000: Optional[str]
    customfield_20000: Optional[str]
    # Add other fields dynamically
    other_fields: Optional[Dict[str, Any]] = {}

class Issue(BaseModel):
    id: Optional[str]
    key: Optional[str]
    fields: Optional[IssueFields]

class BulkIssueUpdate(BaseModel):
    issueUpdates: List[Dict[str, Any]]

class BulkFetchRequest(BaseModel):
    issueIdsOrKeys: List[str]
    fields: Optional[List[str]] = None
    fieldIds: Optional[List[str]] = None
    maxResults: Optional[int] = 50
    nextPageToken: Optional[str] = None

class IssueAssigneeUpdate(BaseModel):
    accountId: str

class IssueNotifyPayload(BaseModel):
    htmlBody: str
    textBody: str
    subject: str
    restrict: Optional[Dict[str, Any]] = None
    to: Optional[Dict[str, Any]] = None
