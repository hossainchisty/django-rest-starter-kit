"""
API v1 URL Configuration

Main URL router for API version 1.
"""
from django.urls import path, include

app_name = "v1"

urlpatterns = [
    # Authentication endpoints (JWT)
    path("auth/", include("apps.users.urls")),
]
