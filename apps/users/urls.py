"""
User URL Configuration
"""
from django.urls import path
from .views import UserRegistrationView, UserProfileView, ChangePasswordView, CustomTokenObtainPairView

app_name = "users"

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
]
