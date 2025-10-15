# app/services/issue_service.py
import requests
from requests.auth import HTTPBasicAuth
from typing import List, Dict, Any
from config import JIRA_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN
from Schema.issue_schema import Issue, BulkIssueUpdate

auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
headers = {"Accept": "application/json", "Content-Type": "application/json"}

class IssueService:

    @staticmethod
    def bulk_fetch(payload: Dict[str, Any]) -> List[Issue]:
        url = f"{JIRA_BASE_URL}/rest/api/2/changelog/bulkfetch"
        response = requests.post(url, headers=headers, auth=auth, json=payload)
        response.raise_for_status()
        return [Issue(**issue) for issue in response.json()]

    @staticmethod
    def get_events() -> List[Dict]:
        url = f"{JIRA_BASE_URL}/rest/api/2/events"
        response = requests.get(url, headers=headers, auth=auth)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def create_issue(payload: Dict[str, Any]) -> Issue:
        url = f"{JIRA_BASE_URL}/rest/api/2/issue"
        response = requests.post(url, headers=headers, auth=auth, json=payload)
        response.raise_for_status()
        return Issue(**response.json())

    @staticmethod
    def bulk_issue_update(payload: Dict[str, Any]) -> Dict:
        url = f"{JIRA_BASE_URL}/rest/api/2/issue/bulk"
        response = requests.post(url, headers=headers, auth=auth, json=payload)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def bulk_fetch_issues(payload: Dict[str, Any]) -> Dict:
        url = f"{JIRA_BASE_URL}/rest/api/2/issue/bulkfetch"
        response = requests.post(url, headers=headers, auth=auth, json=payload)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_issue(issue_id_or_key: str) -> Issue:
        url = f"{JIRA_BASE_URL}/rest/api/2/issue/{issue_id_or_key}"
        response = requests.get(url, headers=headers, auth=auth)
        response.raise_for_status()
        return Issue(**response.json())

    @staticmethod
    def update_issue(issue_id_or_key: str, payload: Dict[str, Any]) -> Issue:
        url = f"{JIRA_BASE_URL}/rest/api/2/issue/{issue_id_or_key}"
        response = requests.put(url, headers=headers, auth=auth, json=payload)
        response.raise_for_status()
        return Issue(**response.json())

    @staticmethod
    def delete_issue(issue_id_or_key: str) -> Dict:
        url = f"{JIRA_BASE_URL}/rest/api/2/issue/{issue_id_or_key}"
        response = requests.delete(url, headers=headers, auth=auth)
        response.raise_for_status()
        return {"status": "deleted", "issue": issue_id_or_key}

    @staticmethod
    def update_assignee(issue_id_or_key: str, payload: Dict[str, Any]) -> Dict:
        url = f"{JIRA_BASE_URL}/rest/api/2/issue/{issue_id_or_key}/assignee"
        response = requests.put(url, headers=headers, auth=auth, json=payload)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def notify_issue(issue_id_or_key: str, payload: Dict[str, Any]) -> Dict:
        url = f"{JIRA_BASE_URL}/rest/api/2/issue/{issue_id_or_key}/notify"
        response = requests.post(url, headers=headers, auth=auth, json=payload)
        response.raise_for_status()
        return response.json()
