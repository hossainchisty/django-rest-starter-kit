"""
Core Models

Abstract base models for common functionality across the application.
"""
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStamp(models.Model):
    """
    Abstract base model that provides self-updating
    'created_at' and 'updated_at' fields.
    """

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]

