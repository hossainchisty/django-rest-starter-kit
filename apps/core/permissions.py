"""
Core Permissions

Custom permission classes for fine-grained access control.
"""
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Permission to only allow owners of an object to access it.
    
    Assumes the model has a 'user' field.
    """

    def has_object_permission(self, request, view, obj):
        """Check if the user is the owner of the object"""
        return obj.user == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission to allow read-only access to everyone,
    but write access only to the owner.
    """

    def has_object_permission(self, request, view, obj):
        """Allow read access to everyone, write access to owner only"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsVerifiedUser(permissions.BasePermission):
    """
    Permission to only allow verified users to access the view.
    """

    message = "You must verify your email address to perform this action."

    def has_permission(self, request, view):
        """Check if user is authenticated and verified"""
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_verified
        )
