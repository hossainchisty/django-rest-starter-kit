"""
Testing Settings

Settings optimized for running tests.
"""
from .base import *  # noqa

# Use in-memory database for faster tests
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Disable migrations for faster tests
class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


MIGRATION_MODULES = DisableMigrations()

# Password hashers - Use fast hasher for tests
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# Email - Use memory backend for tests
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Disable throttling in tests
REST_FRAMEWORK["DEFAULT_THROTTLE_CLASSES"] = []  # noqa
REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {}  # noqa

# Logging - Minimal logging in tests
LOGGING["loggers"]["django"]["level"] = "ERROR"  # noqa
LOGGING["loggers"]["apps"]["level"] = "ERROR"  # noqa

# Disable CSRF for tests
MIDDLEWARE = [m for m in MIDDLEWARE if m != "django.middleware.csrf.CsrfViewMiddleware"]  # noqa
