from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class LoginAPITests(APITestCase):
    def setUp(self):
        self.email = "test@example.com"
        self.password = "testpass123"
        self.user = User.objects.create_user(
            email=self.email, password=self.password, first_name="Test", last_name="User"
        )
        self.login_url = reverse("v1:users:login")

    def test_login_success(self):
        """Test that login returns tokens and user details"""
        data = {
            "email": self.email,
            "password": self.password,
        }
        response = self.client.post(self.login_url, data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("user", response.data)
        
        user_data = response.data["user"]
        self.assertEqual(user_data["email"], self.email)
        self.assertEqual(user_data["first_name"], "Test")
        self.assertEqual(user_data["last_name"], "User")

    def test_login_invalid_credentials(self):
        """Test login with invalid password"""
        data = {
            "email": self.email,
            "password": "wrongpassword",
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_missing_fields(self):
        """Test login with missing fields"""
        data = {
            "email": self.email,
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
