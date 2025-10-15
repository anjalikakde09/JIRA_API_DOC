# app/services/task_service.py
import requests
from requests.auth import HTTPBasicAuth
from config import JIRA_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN
from Schema.task_schema import Task
from typing import Dict

auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
headers = {"Accept": "application/json", "Content-Type": "application/json"}

class TaskService:

    @staticmethod
    def get_task(task_id: str) -> Task:
        url = f"{JIRA_BASE_URL}/rest/api/2/task/{task_id}"
        response = requests.get(url, headers=headers, auth=auth)
        response.raise_for_status()
        return Task(**response.json())

    @staticmethod
    def cancel_task(task_id: str) -> Dict:
        url = f"{JIRA_BASE_URL}/rest/api/2/task/{task_id}/cancel"
        response = requests.post(url, headers=headers, auth=auth)
        response.raise_for_status()
        return {"status": "cancelled", "task": task_id}
