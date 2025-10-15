# app/main.py
from fastapi import FastAPI
from controllers import project_controller, task_controller, issue_controller

app = FastAPI(title="Jira API FastAPI Wrapper")

app.include_router(project_controller.router)
app.include_router(task_controller.router)
app.include_router(issue_controller.router)
