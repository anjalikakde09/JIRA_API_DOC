
# Jira REST API FastAPI Wrapper

A **FastAPI-based wrapper** for Jira REST APIs, providing structured endpoints.

## **API Endpoints**

### **Projects Endpoints**

| Method | Endpoint                                  | Description                     |
| ------ | ----------------------------------------- | ------------------------------- |
| GET    | /projects/                                | Get all projects                |
| GET    | /projects/recent                          | Get recent projects             |
| GET    | /projects/{project_id}                    | Get project by ID               |
| POST   | /projects/                                | Create new project              |
| PUT    | /projects/{project_id}                    | Update project                  |
| DELETE | /projects/{project_id}                    | Delete project                  |
| GET    | /projects/{project_id}/statuses           | Get project statuses            |
| GET    | /projects/{project_id}/hierarchy          | Get project hierarchy           |
| GET    | /projects/{project_id}/notificationscheme | Get project notification scheme |

### **Tasks Endpoints**

| Method | Endpoint                | Description    |
| ------ | ----------------------- | -------------- |
| GET    | /tasks/{task_id}        | Get task by ID |
| POST   | /tasks/{task_id}/cancel | Cancel task    |

### **Issues Endpoints**

| Method | Endpoint                           | Description                 |
| ------ | ---------------------------------- | --------------------------- |
| POST   | /issues/changelog/bulkfetch        | Bulk fetch issue changelogs |
| GET    | /issues/events                     | Get Jira events             |
| POST   | /issues/                           | Create a new issue          |
| POST   | /issues/bulk                       | Bulk update issues          |
| POST   | /issues/bulkfetch                  | Bulk fetch issues           |
| GET    | /issues/{issue_id_or_key}          | Get issue by ID or key      |
| PUT    | /issues/{issue_id_or_key}          | Update issue                |
| DELETE | /issues/{issue_id_or_key}          | Delete issue                |
| PUT    | /issues/{issue_id_or_key}/assignee | Update issue assignee       |
| POST   | /issues/{issue_id_or_key}/notify   | Send notification for issue |

---

