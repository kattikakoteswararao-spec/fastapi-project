# FastAPI User Management REST API

## Overview

This project is a production-style REST API built using FastAPI for managing users.

The application provides CRUD operations, pagination, filtering, database persistence, validation, logging, centralized error handling, API documentation, and automated tests.

## Technologies Used

Python
FastAPI
Pydantic
SQLAlchemy
SQLite
Pytest
HTTPX
python-dotenv
Uvicorn

## Project Architecture

The application follows a layered architecture:

API/Router → Service → Repository → Database

### Layers

**Router** - Handles HTTP requests and responses.
**Service** - Contains business logic.
**Repository** - Handles database operations.
**Model** - Defines database tables.
**Schema** - Defines request and response validation.
**Core** - Contains logging and centralized exception handling.
**Tests** - Contains API/integration tests.

## Project Structure

textfastapi-project/
│
├── app/
│   ├── core/
│   │   ├── exception_handlers.py
│   │   └── logging_config.py
│   │
│   ├── database/
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── repositories/
│   │   └── user_repository.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── users.py
│   │
│   ├── schemas/
│   │   └── user.py
│   │
│   ├── services/
│   │   └── user_service.py
│   │
│   └── main.py
│
├── tests/
│   └── test_users.py
│
├── .env
├── .gitignore
└── README.md

Features:

CRUD APIs

Create user
Get all users
Get user by ID
Update user
Delete user

Pagination

Users can be retrieved using:
GET /users/?skip=0&limit=10

Filtering

Users can be filtered by name:
GET /users/?name=Test

Validation

Pydantic schemas are used to validate API request and response data.

Database

The application uses SQLite with SQLAlchemy ORM for database persistence.

The database configuration can be controlled using environment variables.

Logging

Application logging is configured using a centralized logging configuration.

Error Handling

A centralized exception handler is implemented for unexpected application errors.

API endpoints also return appropriate HTTP errors such as 404 Not Found.

Running the Application

Activate the virtual environment:
.\venv\Scripts\Activate.ps1

Install dependencies:

pip install fastapi uvicorn sqlalchemy pydantic python-dotenv pytest httpx

Start the application:

uvicorn app.main:app --reload

The API will be available at:
http://127.0.0.1:8000

API Documentation

FastAPI automatically provides Swagger/OpenAPI documentation.

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

Testing

The project contains API/integration tests using Pytest and FastAPI TestClient.

Run all tests:

python -m pytest -v

Current test coverage includes:
User creation
Get users
Pagination
Name filtering
User-not-found handling
Delete-user error handling
All 5 tests are currently passing.
Configuration
Environment variables are loaded using python-dotenv.
Example:

DATABASE_URL=sqlite:///./users.db

This allows database configuration to be changed without modifying application code.

Example API Endpoints

Method
Endpoint
Description
POST
/users/
Create a user
GET
/users/
Get users
GET
/users/{user_id}
Get user by ID
PUT
/users/{user_id}
Update a user
DELETE
/users/{user_id}
Delete a user

Conclusion

This project demonstrates a clean FastAPI REST service with layered architecture, database integration, validation, pagination, filtering, logging, centralized error handling, environment configuration, API documentation, and automated testing.

## Architecture Diagram

'''mermaid
flowchart TD
    A[Client / Swagger UI] --> B[FastAPI Router]
    B --> C[Pydantic Schema Validation]
    C --> D[Service Layer]
    D --> E[Repository Layer]
    E --> F[SQLAlchemy ORM]
    F --> G[(SQLite Database)]

    H[Environment Variables] --> F
    I[Logging Configuration] --> B
    J[Centralized Exception Handler] --> B
    K[Pytest API Tests] --> B
 '''   


Architecture Flow;

Client / Swagger
       |
       v
 FastAPI Router
       |
       v
 Pydantic Validation
       |
       v
  Service Layer
       |
       v
 Repository Layer
       |
       v
 SQLAlchemy ORM
       |
       v
 SQLite Database

Testing: Pytest + FastAPI TestClient

Cross-cutting components: Logging, Exception Handling, Environment Configuration