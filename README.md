# Gym Management System API

This project implements a CRUD API for a gym management system using Django REST Framework. It allows users to manage gyms, trainers, clients, and workout sessions.

## API Testing (Postman)
- **Postman collection**
    ```
    https://www.postman.com/sachinkant/workspace/sachin-s-workspace/collection/25924538-ef599dda-580d-47b1-8f9b-11868a9e9332?action=share&creator=25924538
    ```
- **Postman Documentation**
    ```
    https://documenter.getpostman.com/view/25924538/2s9YRB3sLs
    ```

## Requirements

- Python
- Django
- Django REST Framework

## Project Structure
```
gym
├── api
│   └── urls.py
├── gym
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── gymapp
│   ├── admin.py
│   ├── apps.py
│   ├── auth.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── README.md
```


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sachin-404/gym-management-system-api.git
    ```
2. Create a virtual environment:
    ```
    python3 -m venv venv
    ```
3. Activate the virtual environment:
    - Linux/macOS:
        ```
        source venv/bin/activate
        ```
    - Windows:
        ```
        venv\Scripts\activate
        ```

4. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

5. Apply migrations:
    ```
    python manage.py migrate
    ```

6. Run the development server:
    ```
    python manage.py runserver
    ```

## Usage
1. Create gyms, trainers, clients, and workout sessions using the API endpoints.
2. Access the API at http://127.0.0.1:8000/api/.
2. Access the API documentation (swagger UI) at http://127.0.0.1:8000/api/docs/.

## API Endpoints
- /gyms/: CRUD operations for gyms.
- /trainers/: CRUD operations for trainers.
- /clients/: CRUD operations for clients.
- /workoutsessions/: CRUD operations for workout sessions.
