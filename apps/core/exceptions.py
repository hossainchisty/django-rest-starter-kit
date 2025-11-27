"""
Core Exceptions

Custom exception classes and exception handler for the API.
"""
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework import status


def custom_exception_handler(exc, context):
    """
    Custom exception handler that provides consistent error responses.
    
    Returns:
        Response with standardized error format:
        {
            "error": {
                "message": "Error message",
                "code": "error_code",
                "details": {...}
            }
        }
    """
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)

    if response is not None:
        # Customize the response data
        custom_response_data = {
            "error": {
                "message": str(exc),
                "code": getattr(exc, "default_code", "error"),
            }
        }
        
        # Add details if available
        if hasattr(exc, "detail"):
            custom_response_data["error"]["details"] = exc.detail
        
        response.data = custom_response_data

    return response


class ServiceUnavailable(APIException):
    """Exception for service unavailable errors"""
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = "Service temporarily unavailable, try again later."
    default_code = "service_unavailable"


class BadRequest(APIException):
    """Exception for bad request errors"""
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Bad request."
    default_code = "bad_request"
