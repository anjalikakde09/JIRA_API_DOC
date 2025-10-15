from dotenv import load_dotenv
import os

load_dotenv()

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

if not all([JIRA_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN]):
    raise ValueError("Missing Jira configuration in .env")

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
JIRA_AUTH = (JIRA_EMAIL, JIRA_API_TOKEN)
