from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse


class AuthUserTests(APITestCase):
    def setUp(self):
        self.data = {
            'username': 'michael',
            'first_name': 'Michael',
            'last_name': 'Wood',
            'email': 'michael_wood@gmail.com',
            'password': '@password@',
            'is_active': True
        }
        User.objects.create_user(**self.data)
        self.url = reverse('user:user-sign_in')

    def test_sign_in_success_response(self):
        data = {
            'username': self.data.get('username'),
            'password': self.data.get('password')
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)

    def test_sign_in_fail_response(self):
        data = {
            "username": "testuser",
            "password": "testpassword"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 401)
