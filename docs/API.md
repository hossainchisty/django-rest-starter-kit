# API Documentation

The API is built using Django REST Framework and follows RESTful principles.

## Base URL

- Development: `http://localhost:8000/api/v1/`
- Production: `https://api.yourdomain.com/api/v1/`

## Authentication

The API uses JWT (JSON Web Token) authentication.

### 1. Obtain Token
**POST** `/token/`

Request:
```json
{
    "email": "user@example.com",
    "password": "strongpassword"
}
```

Response:
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 2. Use Token
Include the access token in the `Authorization` header of your requests:
```
Authorization: Bearer <your_access_token>
```

### 3. Refresh Token
**POST** `/token/refresh/`

Request:
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

## Endpoints

### User Management

#### Register User
**POST** `/auth/register/`

Request:
```json
{
    "email": "newuser@example.com",
    "password": "password123",
    "password2": "password123",
    "first_name": "John",
    "last_name": "Doe"
}
```

#### Get Profile
**GET** `/auth/profile/`
*Requires Authentication*

Response:
```json
{
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "is_verified": false,
    "date_joined": "2024-03-20T10:00:00Z"
}
```

#### Update Profile
**PATCH** `/auth/profile/`
*Requires Authentication*

Request:
```json
{
    "first_name": "Jane"
}
```

#### Change Password
**POST** `/auth/change-password/`
*Requires Authentication*

Request:
```json
{
    "old_password": "oldpassword",
    "new_password": "newpassword",
    "new_password2": "newpassword"
}
```

## Error Handling

Errors are returned in a consistent JSON format:

```json
{
    "error": {
        "message": "Error description",
        "code": "error_code",
        "details": {
            "field_name": ["Error detail"]
        }
    }
}
```

Common HTTP Status Codes:
- `200 OK`: Request successful
- `201 Created`: Resource created
- `400 Bad Request`: Validation error
- `401 Unauthorized`: Authentication failed
- `403 Forbidden`: Permission denied
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

## Pagination

List endpoints support pagination using query parameters:
- `page`: Page number (default: 1)
- `page_size`: Items per page (default: 50)

Response format:
```json
{
    "count": 100,
    "next": "http://api.example.com/resource/?page=2",
    "previous": null,
    "results": [...]
}
```

## Filtering & Searching

- **Search**: `?search=query`
- **Ordering**: `?ordering=field_name` (prefix with `-` for descending)
- **Filtering**: `?field_name=value`
