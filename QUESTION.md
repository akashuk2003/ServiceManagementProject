Task: Develop a Basic Service Management Module using Django and Django REST Framework.

1. Database Model Creation
• Create a Django app named service.
• Create a model named Services with following fiedsservice_name, description, price, duration, status, created_at, updated_at

2. REST API Development
• Develop the following APIs:
a. Create Service
b. List Services
c. Service Details
d. Update Service
e. Delete Service
• API requirements:
Implement validation, Handle invalid IDs, Return proper HTTP status codes,
Implement pagination, Search by service name, Filter by status.

3. HTML Admin Panel Development
• Develop a separate HTML-based management interface using Django Views and
Templates.
Service List, Add Service, Edit Service, Service Details, Delete Service
• Frontend requirements:
Search services by name, Active/inactive filtering, Pagination, Form validation.
Note:
• The REST API and HTML CRUD must be implemented separately. The HTML interface
must use Django Views, Forms and Templates, not call the REST APIs through Js.
• Use SQLite as the database.