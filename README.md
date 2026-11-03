# Service Management Module

A Service Management application developed using Django and Django REST Framework.

## Features

### REST API
- Create, list, retrieve, update, and delete services
- Input validation
- Search services by name
- Filter services by status
- API pagination
- Appropriate HTTP status codes

### HTML Admin Panel
- Create, view, update, and delete services
- Search and filter services
- Paginated service listing
- Django ModelForms with validation
- Delete confirmation
- Separate HTML views and REST API views

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- HTML

## Service Model

| Field | Type |
|---|---|
| service_name | CharField |
| description | TextField |
| price | DecimalField |
| duration | DurationField |
| status | CharField |
| created_at | DateTimeField |
| updated_at | DateTimeField |

## Installation

Clone the repository:

```bash
git clone
cd service-management
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows:
```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

## HTML Admin Panel

- Service List: http://127.0.0.1:8000/services/
- Create Service: http://127.0.0.1:8000/services/create/

## REST API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /api/services/ | List services |
| POST | /api/services/ | Create service |
| GET | /api/services/{id}/ | Retrieve service |
| PUT | /api/services/{id}/ | Update service |
| PATCH | /api/services/{id}/ | Partial update |
| DELETE | /api/services/{id}/ | Delete service |

### Search and Filtering

```text
/api/services/?name=web
/api/services/?status=PENDING
/api/services/?name=web&status=PENDING
```

## Pagination

API and HTML service listing support pagination.

## Database

SQLite is used as the database.

