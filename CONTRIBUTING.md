# Contributing to Django REST Framework Starter Kit

First off, thank you for considering contributing to Django REST Framework Starter Kit! It's people like you that make this project such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if relevant**
- **Include your environment details** (OS, Python version, Django version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any similar features in other projects**

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Follow the coding standards** outlined below
3. **Write tests** for your changes
4. **Ensure all tests pass**
5. **Update documentation** as needed
6. **Write a clear commit message**

## Development Setup

### 1. Fork and Clone

```bash
git clone https://github.com/hossainchisty/django-rest-starter-kit.git
cd django-rest-starter-kit
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements/development.txt
```

### 4. Set Up Pre-commit Hooks

```bash
pre-commit install
```

### 5. Create .env File

```bash
cp .env.example .env
# Edit .env with your settings
```

### 6. Run Migrations

```bash
python manage.py migrate
```

## Coding Standards

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

- **Line length**: 100 characters (Black default)
- **Use Black** for code formatting
- **Use isort** for import sorting
- **Use type hints** where appropriate

### Code Formatting

Before committing, format your code:

```bash
# Format with Black
black .

# Sort imports with isort
isort .

# Or use the Makefile
make format
```

### Linting

Run linters to check code quality:

```bash
# Flake8
flake8

# Pylint
pylint apps/

# Or use the Makefile
make lint
```

### Type Checking

```bash
mypy apps/
```

## Testing Guidelines

### Writing Tests

- Write tests for all new features and bug fixes
- Use pytest for testing
- Use factory_boy for test data generation
- Aim for >80% code coverage

### Test Structure

```python
# apps/users/tests/test_models.py
import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestUserModel:
    def test_create_user(self):
        user = User.objects.create_user(
            email="test@example.com",
            password="testpass123"
        )
        assert user.email == "test@example.com"
        assert user.check_password("testpass123")
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=apps --cov-report=html

# Run specific test file
pytest apps/users/tests/test_models.py

# Run specific test
pytest apps/users/tests/test_models.py::TestUserModel::test_create_user
```

## Documentation

### Docstrings

Use Google-style docstrings:

```python
def function_name(param1: str, param2: int) -> bool:
    """
    Brief description of the function.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: Description of when this is raised
    """
    pass
```

### Code Comments

- Write self-documenting code when possible
- Use comments to explain **why**, not **what**
- Keep comments up-to-date with code changes

## Git Workflow

### Branch Naming

- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `hotfix/description` - Urgent fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Example:
```
feat(users): add email verification

- Add email verification model
- Create verification email template
- Add verification endpoint

Closes #123
```

### Pull Request Process

1. **Update your fork** with the latest changes from main
2. **Create a new branch** for your feature/fix
3. **Make your changes** following the coding standards
4. **Write/update tests** for your changes
5. **Run tests and linters** to ensure everything passes
6. **Update documentation** if needed
7. **Push to your fork** and create a pull request
8. **Fill out the PR template** completely
9. **Wait for review** and address any feedback

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Checklist
- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated

## Related Issues
Closes #(issue number)
```

## Project Structure Guidelines

### Adding New Apps

1. Create app in `apps/` directory
2. Add to `INSTALLED_APPS` in `config/settings/base.py`
3. Create tests directory with `__init__.py`
4. Add URL configuration if needed
5. Update documentation

### File Organization

```
apps/your_app/
├── __init__.py
├── apps.py
├── models.py
├── serializers.py
├── views.py
├── urls.py
├── admin.py
├── permissions.py
├── signals.py
├── utils.py
└── tests/
    ├── __init__.py
    ├── factories.py
    ├── test_models.py
    ├── test_views.py
    └── test_serializers.py
```

## Questions?

Feel free to:
- Open an issue for discussion
- Join our community discussions
- Reach out to maintainers

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing! 🎉
