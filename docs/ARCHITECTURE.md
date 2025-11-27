# Architecture Documentation

## Overview

The Django REST Starter Kit follows a modular, scalable architecture designed for production-ready applications. It emphasizes separation of concerns, reusability, and maintainability.

## Project Structure

The project is organized into the following main components:

```
django-rest-starter-kit/
├── apps/               # Domain-specific applications
├── config/             # Project configuration
├── requirements/       # Dependency management
└── docs/               # Documentation
```

### Apps Directory (`apps/`)

All business logic resides in the `apps/` directory. Each app is a self-contained Python package with its own models, views, serializers, and tests.

- **`core/`**: Contains shared functionality used across the project.
  - Abstract base models (`TimeStampedModel`, `UUIDModel`)
  - Custom permissions
  - Utility functions
  - Middleware
  - Exception handlers

- **`users/`**: Handles user management and authentication.
  - Custom User model (email-based)
  - Registration and profile management
  - Authentication views

- **`api/`**: Handles API versioning and routing.
  - Centralized URL configuration for different API versions (v1, v2)

### Configuration (`config/`)

The configuration is split into environment-specific modules:

- **`settings/base.py`**: Common settings shared across all environments.
- **`settings/development.py`**: Settings for local development (debug mode, console email).
- **`settings/production.py`**: Settings for production (security, caching, S3).
- **`settings/testing.py`**: Settings optimized for running tests.

## Key Design Decisions

### 1. Custom User Model

We use a custom user model (`apps.users.models.User`) extending `AbstractBaseUser`.
- **Why**: To use email as the primary identifier instead of username, and to allow easy extension of the user profile in the future.
- **Benefit**: More modern authentication flow and flexibility.

### 2. API Versioning

API routes are versioned (e.g., `/api/v1/`).
- **Why**: To allow breaking changes in future versions without affecting existing clients.
- **Implementation**: `apps/api/v1/urls.py` handles routing for version 1.

### 3. JWT Authentication

We use JSON Web Tokens (JWT) via `djangorestframework-simplejwt`.
- **Why**: Stateless authentication suitable for SPAs and mobile apps.
- **Flow**: Client exchanges credentials for Access and Refresh tokens.

### 4. Abstract Base Models

Common fields like `created_at`, `updated_at`, and `id` (UUID) are defined in abstract base models in `apps.core.models`.
- **Why**: To enforce consistency across all models and reduce code duplication.

### 5. Environment-Based Settings

Settings are split by environment.
- **Why**: To keep production secrets safe and allow different configurations for dev/prod/test without conditional logic in a single file.

## Data Flow

1. **Request**: Client sends HTTP request to Nginx/Gunicorn.
2. **Middleware**: Request passes through security and logging middleware.
3. **URL Routing**: Django resolves URL to a specific view in `apps/`.
4. **Authentication/Permission**: DRF checks JWT token and user permissions.
5. **View**: View processes request, interacts with Services/Models.
6. **Serializer**: Data is validated and serialized to JSON.
7. **Response**: JSON response is returned to client.

## Database Schema

### Users Table
- `id`: UUID (Primary Key)
- `email`: String (Unique, Indexed)
- `password`: Hash
- `first_name`: String
- `last_name`: String
- `is_active`: Boolean
- `is_staff`: Boolean
- `is_verified`: Boolean
- `date_joined`: DateTime
- `updated_at`: DateTime

## Security

- **Password Hashing**: Argon2 (production) / PBKDF2
- **HTTPS**: Enforced in production settings
- **CORS**: Whitelisted origins only
- **Rate Limiting**: Throttling enabled for API endpoints

## Scalability

- **Stateless API**: Ready for horizontal scaling behind a load balancer.
- **Caching**: Redis configured for caching and session storage.
- **Task Queue**: Ready for Celery integration (async tasks).
- **Database**: PostgreSQL recommended for production.
