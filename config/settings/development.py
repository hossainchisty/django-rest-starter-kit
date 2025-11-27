"""
Development Settings

Settings for local development environment.
"""
from .base import *  # noqa

# Debug mode
DEBUG = True

# Allowed hosts for development
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

# Database - SQLite for development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa
    }
}

# CORS - Allow all origins in development
CORS_ALLOW_ALL_ORIGINS = True

# Email - Console backend for development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Disable throttling in development
REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {  # noqa
    "anon": "10000/hour",
    "user": "100000/hour",
}

# Add browsable API renderer for development
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [  # noqa
    "rest_framework.renderers.JSONRenderer",
    "rest_framework.renderers.BrowsableAPIRenderer",
]

# Logging - More verbose in development
LOGGING["loggers"]["django"]["level"] = "DEBUG"  # noqa
LOGGING["loggers"]["apps"]["level"] = "DEBUG"  # noqa

# Django Debug Toolbar (optional - uncomment if installed)
# INSTALLED_APPS += ["debug_toolbar"]  # noqa
# MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa
# INTERNAL_IPS = ["127.0.0.1"]
