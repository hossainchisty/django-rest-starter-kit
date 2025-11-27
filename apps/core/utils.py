"""
Core Utilities

Helper functions and utilities used across the application.
"""
import random
import string
from typing import Optional


def generate_random_string(length: int = 32) -> str:
    """
    Generate a random string of specified length.
    
    Args:
        length: Length of the string to generate (default: 32)
        
    Returns:
        Random string containing letters and digits
    """
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def generate_verification_code(length: int = 6) -> str:
    """
    Generate a numeric verification code.
    
    Args:
        length: Length of the code (default: 6)
        
    Returns:
        Numeric verification code as string
    """
    return "".join(random.choice(string.digits) for _ in range(length))


def normalize_email(email: str) -> str:
    """
    Normalize email address to lowercase.
    
    Args:
        email: Email address to normalize
        
    Returns:
        Normalized email address
    """
    return email.lower().strip()


def get_client_ip(request) -> Optional[str]:
    """
    Get client IP address from request.
    
    Args:
        request: Django request object
        
    Returns:
        Client IP address or None
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
