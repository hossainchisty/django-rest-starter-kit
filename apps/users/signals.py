"""
User Signals

Signal handlers for user-related events.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    """
    Signal handler for post-save events on User model.
    
    Args:
        sender: The model class (User)
        instance: The actual instance being saved
        created: Boolean indicating if this is a new instance
    """
    if created:
        # Add any post-creation logic here
        # For example: send welcome email, create user profile, etc.
        pass
