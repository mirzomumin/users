from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse


class CreateUserTests(APITestCase):
    def setUp(self):
        self.user_1_data = {
            'username': 'michael',
            'first_name': 'Michael',
            'last_name': 'Wood',
            'email': 'michael_wood@gmail.com',
            'password1': '@password@',
            'password2': '@password@'
        }
        self.user_2_data = {
            'username': 'michael',
            'first_name': 'Michael',
            'last_name': 'Freeman',
            'email': 'michael@gmail.com'
        }

    def test_sign_up_success_response(self):
        url = reverse('user:user-list')
        response = self.client.post(url, self.user_1_data)
        self.assertEqual(response.status_code, 201)

    def test_sign_up_fail_response(self):
        url = reverse('user:user-list')
        data = {}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)

        # Unique username
        User.objects.create(**self.user_2_data)
        response = self.client.post(url, self.user_1_data)
        self.assertEqual(response.json().get('username')[0], 'A user with that username already exists.')
