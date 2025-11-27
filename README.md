# Django REST Framework Starter Kit

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/django-5.0-green.svg)](https://www.djangoproject.com/)
[![DRF Version](https://img.shields.io/badge/drf-3.15-red.svg)](https://www.django-rest-framework.org/)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A professional, production-ready Django REST Framework starter kit with best practices, comprehensive documentation, and modern development tooling.

## ✨ Features

### 🔐 Authentication & User Management
- **Custom User Model** with email-based authentication
- **JWT Authentication** with access and refresh tokens
- **User Registration** with email validation
- **Profile Management** endpoints
- **Password Change** functionality
- Token blacklisting support

### 🏗️ Architecture
- **Modular App Structure** for scalability
- **Environment-based Settings** (development, production, testing)
- **Abstract Base Models** for timestamps and UUIDs
- **Custom Exception Handling** with consistent error responses
- **API Versioning** structure (v1, v2, etc.)

### 📚 API Features
- **Comprehensive API Documentation** with Swagger/ReDoc
- **Pagination** with customizable page sizes
- **Filtering, Searching & Ordering** out of the box
- **Rate Limiting** to prevent abuse
- **CORS** configuration for cross-origin requests

### 🛠️ Development Tools
- **Docker & Docker Compose** for containerized development
- **Pre-commit Hooks** for code quality
- **Code Formatting** with Black and isort
- **Linting** with Flake8 and Pylint
- **Type Checking** with mypy
- **Makefile** for common commands

### ✅ Testing
- **Pytest** configuration with Django support
- **Test Factories** with factory_boy
- **Code Coverage** reporting
- **Example Tests** for models, views, and serializers

### 🚀 Production Ready
- **Security Settings** for production deployment
- **Logging Configuration** with file and console handlers
- **Caching Support** (Redis)
- **Database Support** (PostgreSQL, MySQL, SQLite)
- **Static & Media Files** configuration
- **CI/CD** with GitHub Actions

## 📋 Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- virtualenv or venv (recommended)
- PostgreSQL or MySQL (for production)
- Redis (optional, for caching)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/hossainchisty/django-rest-starter-kit.git
cd django-rest-starter-kit
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\\Scripts\\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install development dependencies
pip install -r requirements.txt

# Or install production dependencies
pip install -r requirements/production.txt
```

### 4. Environment Configuration

```bash
# Copy example environment file
cp .env.example .env

# Edit .env file with your settings
# Generate a new SECRET_KEY:
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 5. Database Setup

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

### 7. Access API Documentation

- **Swagger UI**: http://127.0.0.1:8000/swagger/
- **ReDoc**: http://127.0.0.1:8000/redoc/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 🐳 Docker Setup

### Using Docker Compose

```bash
# Build and start containers
docker-compose up --build

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Stop containers
docker-compose down
```

## 📁 Project Structure

```
django-rest-starter-kit/
├── apps/                       # Application modules
│   ├── api/                   # API versioning
│   │   └── v1/               # API version 1
│   ├── core/                 # Core functionality
│   │   ├── models.py        # Abstract base models
│   │   ├── permissions.py   # Custom permissions
│   │   ├── pagination.py    # Pagination classes
│   │   ├── exceptions.py    # Exception handlers
│   │   └── utils.py         # Utility functions
│   └── users/               # User management
│       ├── models.py        # Custom user model
│       ├── serializers.py   # User serializers
│       ├── views.py         # User endpoints
│       └── admin.py         # Admin configuration
├── config/                   # Project configuration
│   ├── settings/            # Split settings
│   │   ├── base.py         # Base settings
│   │   ├── development.py  # Development settings
│   │   ├── production.py   # Production settings
│   │   └── testing.py      # Testing settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
├── docs/                    # Documentation
├── requirements/            # Requirements files
│   ├── base.txt           # Base dependencies
│   ├── development.txt    # Dev dependencies
│   ├── production.txt     # Production dependencies
│   └── testing.txt        # Testing dependencies
├── static/                 # Static files
├── media/                  # Media files
├── logs/                   # Log files
├── .env.example           # Environment variables example
├── .gitignore            # Git ignore rules
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile            # Docker configuration
├── Makefile              # Common commands
├── manage.py             # Django management script
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables

Key environment variables in `.env`:

```bash
# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
DJANGO_SETTINGS_MODULE=config.settings.development
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-password

# Redis
REDIS_URL=redis://127.0.0.1:6379/1
```

See `.env.example` for all available options.

### Settings Modules

- **Development**: `config.settings.development`
- **Production**: `config.settings.production`
- **Testing**: `config.settings.testing`

Switch between environments:
```bash
export DJANGO_SETTINGS_MODULE=config.settings.production
```

## 📡 API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/token/` | Obtain JWT token pair |
| POST | `/api/v1/token/refresh/` | Refresh access token |
| POST | `/api/v1/token/verify/` | Verify token validity |

### User Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register/` | Register new user |
| GET | `/api/v1/auth/profile/` | Get user profile |
| PUT/PATCH | `/api/v1/auth/profile/` | Update user profile |
| POST | `/api/v1/auth/change-password/` | Change password |

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=apps --cov-report=html

# Run specific test file
pytest apps/users/tests/test_models.py

# Run with verbose output
pytest -v
```

## 🎨 Code Quality

```bash
# Format code
black .
isort .

# Lint code
flake8
pylint apps/

# Type checking
mypy apps/

# Run all checks
make lint
```

## 📦 Makefile Commands

```bash
make install      # Install dependencies
make migrate      # Run database migrations
make migrations   # Create new migrations
make superuser    # Create superuser
make run          # Run development server
make test         # Run tests with coverage
make lint         # Run linters
make format       # Format code
make clean        # Clean cache files
```

## 🚀 Deployment

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed deployment instructions.

### Quick Production Checklist

- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use PostgreSQL or MySQL
- [ ] Set up Redis for caching
- [ ] Configure email backend
- [ ] Set strong `SECRET_KEY`
- [ ] Enable HTTPS/SSL
- [ ] Configure static/media file serving
- [ ] Set up logging and monitoring
- [ ] Run security checks: `python manage.py check --deploy`

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linters
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📄 License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)
- [drf-yasg](https://drf-yasg.readthedocs.io/)

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/hossainchisty/django-rest-starter-kit/issues)
- **Discussions**: [GitHub Discussions](https://github.com/hossainchisty/django-rest-starter-kit/discussions)
- **Email**: contact@example.com

## 🗺️ Roadmap

- [ ] Add email verification
- [ ] Add password reset via email
- [ ] Add social authentication (Google, GitHub)
- [ ] Add API rate limiting per user
- [ ] Add WebSocket support
- [ ] Add GraphQL support
- [ ] Add multi-language support
- [ ] Add comprehensive example app

---

**Made with ❤️ by [Hossain Chisty](https://github.com/hossainchisty)**
