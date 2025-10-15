# app/services/project_service.py
import requests
from requests.auth import HTTPBasicAuth
from config import JIRA_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN
from Schema.project_schema import Project
from typing import List, Dict

auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
headers = {"Accept": "application/json", "Content-Type": "application/json"}

class ProjectService:

    @staticmethod
    def get_all_projects() -> List[Project]:
        url = f"{JIRA_BASE_URL}/rest/api/2/project"
        response = requests.get(url, headers=headers, auth=auth)
        response.raise_for_status()
        return [Project(**proj) for proj in response.json()]

    @staticmethod
    def create_project(payload: Dict) -> Project:
        url = f"{JIRA_BASE_URL}/rest/api/2/project"
        response = requests.post(url, headers=headers, auth=auth, json=payload)
        response.raise_for_status()
        return Project(**response.json())

    @staticmethod
    def get_recent_projects() -> List[Project]:
        url = f"{JIRA_BASE_URL}/rest/api/2/project/recent"
        response = requests.get(url, headers=headers, auth=auth)
        response.raise_for_status()
        return [Project(**proj) for proj in response.json()]

    @staticmethod
    def get_project_by_id(project_id_or_key: str) -> Project:
        url = f"{JIRA_BASE_URL}/rest/api/2/project/{project_id_or_key}"
        response = requests.get(url, headers=headers, auth=auth)
        response.raise_for_status()
        return Project(**response.json())

    @staticmethod
    def update_project(project_id_or_key: str, payload: Dict) -> Project:
        url = f"{JIRA_BASE_URL}/rest/api/2/project/{project_id_or_key}"
        response = requests.put(url, headers=headers, auth=auth, json=payload)
        response.raise_for_status()
        return Project(**response.json())

    @staticmethod
    def delete_project(project_id_or_key: str) -> Dict:
        url = f"{JIRA_BASE_URL}/rest/api/2/project/{project_id_or_key}"
        response = requests.delete(url, headers=headers, auth=auth)
        response.raise_for_status()
        return {"status": "deleted", "project": project_id_or_key}

    @staticmethod
    def get_project_statuses(project_id_or_key: str) -> List[Dict]:
        url = f"{JIRA_BASE_URL}/rest/api/2/project/{project_id_or_key}/statuses"
        response = requests.get(url, headers=headers, auth=auth)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_project_hierarchy(project_id: str) -> Dict:
        url = f"{JIRA_BASE_URL}/rest/api/2/project/{project_id}/hierarchy"
        response = requests.get(url, headers=headers, auth=auth)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_project_notification_scheme(project_id_or_key: str) -> Dict:
        url = f"{JIRA_BASE_URL}/rest/api/2/project/{project_id_or_key}/notificationscheme"
        response = requests.get(url, headers=headers, auth=auth)
        response.raise_for_status()
        return response.json()
