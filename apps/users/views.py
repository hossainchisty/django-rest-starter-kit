"""
User Views

API endpoints for user registration, profile management, and authentication.
"""
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    UserSerializer,
    UserRegistrationSerializer,
    ChangePasswordSerializer,
    UserUpdateSerializer,
    CustomTokenObtainPairSerializer,
)

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    API endpoint for user login.
    
    Returns JWT tokens (access and refresh) along with user details.
    """
    serializer_class = CustomTokenObtainPairSerializer

    @swagger_auto_schema(
        operation_description="Login user and get tokens with user details",
        responses={
            200: openapi.Response("Login successful", CustomTokenObtainPairSerializer),
            401: "Unauthorized - Invalid credentials",
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserRegistrationView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    
    Allows anyone to create a new user account.
    """

    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    @swagger_auto_schema(
        operation_description="Register a new user account",
        responses={
            201: openapi.Response("User created successfully", UserSerializer),
            400: "Bad Request - Validation errors",
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    API endpoint to retrieve and update the authenticated user's profile.
    
    GET: Retrieve current user profile
    PUT/PATCH: Update current user profile
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = UserUpdateSerializer

    def get_object(self):
        """Return the current authenticated user"""
        return self.request.user

    @swagger_auto_schema(
        operation_description="Get current user profile",
        responses={200: UserSerializer},
    )
    def get(self, request, *args, **kwargs):
        """Get user profile"""
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update current user profile",
        responses={
            200: UserSerializer,
            400: "Bad Request - Validation errors",
        },
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Partially update current user profile",
        responses={
            200: UserSerializer,
            400: "Bad Request - Validation errors",
        },
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


class ChangePasswordView(APIView):
    """
    API endpoint for changing user password.
    
    Requires authentication and validates old password before setting new one.
    """

    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_description="Change user password",
        request_body=ChangePasswordSerializer,
        responses={
            200: openapi.Response("Password changed successfully"),
            400: "Bad Request - Validation errors",
        },
    )
    def post(self, request):
        """Change password for authenticated user"""
        serializer = ChangePasswordSerializer(
            data=request.data, context={"request": request}
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"detail": "Password changed successfully."},
                status=status.HTTP_200_OK,
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
