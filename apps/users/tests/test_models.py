import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestUserModel:
    def test_create_user(self):
        """Test creating a new user"""
        email = "test@example.com"
        password = "testpass123"
        user = User.objects.create_user(email=email, password=password)
        
        assert user.email == email
        assert user.check_password(password)
        assert not user.is_staff
        assert not user.is_superuser
        assert user.is_active

    def test_create_superuser(self):
        """Test creating a superuser"""
        email = "admin@example.com"
        password = "adminpass123"
        user = User.objects.create_superuser(email=email, password=password)
        
        assert user.email == email
        assert user.check_password(password)
        assert user.is_staff
        assert user.is_superuser
        assert user.is_active

    def test_create_user_without_email(self):
        """Test creating user without email raises error"""
        with pytest.raises(ValueError):
            User.objects.create_user(email="", password="password")

    def test_create_superuser_without_is_staff(self):
        """Test creating superuser without is_staff raises error"""
        with pytest.raises(ValueError):
            User.objects.create_superuser(
                email="admin@example.com", 
                password="password", 
                is_staff=False
            )
