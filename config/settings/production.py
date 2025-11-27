"""
Production Settings

Settings for production environment with security hardening.
"""
from .base import *  # noqa

# Security
DEBUG = False

# Hosts - Must be set via environment variable
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")  # noqa

# Database - PostgreSQL recommended for production
DATABASES = {
    "default": env.db("DATABASE_URL")  # noqa
}

# Security Settings
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=True)  # noqa
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = "DENY"

# Password Hashers - Use Argon2 for production
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# Email - Use real SMTP in production
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")  # noqa
EMAIL_PORT = env.int("EMAIL_PORT", default=587)  # noqa
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)  # noqa
EMAIL_HOST_USER = env("EMAIL_HOST_USER")  # noqa
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")  # noqa
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")  # noqa

# Static and Media Files
# Use cloud storage (S3, GCS, etc.) in production
# STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME", default="us-east-1")

# Caching - Redis recommended for production
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": env("REDIS_URL", default="redis://127.0.0.1:6379/1"),  # noqa
    }
}

# Session - Use cache backend
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Logging - Log to file in production
LOGGING["handlers"]["file"]["filename"] = env(  # noqa
    "LOG_FILE_PATH",
    default="/var/log/django/django.log",  # noqa
)
LOGGING["loggers"]["django"]["level"] = "WARNING"  # noqa
LOGGING["loggers"]["apps"]["level"] = "INFO"  # noqa

# Admin URL - Change for security
# ADMIN_URL = env("ADMIN_URL", default="admin/")
