from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse


class GetUserTests(APITestCase):
    def setUp(self):
        User.objects.create_user(
            username='nick',
            first_name='Nick',
            last_name='Freeman',
            email='nick@gmail.com',
            password='password',
            is_active=True
        )
        self.data = {
            "username": "nicholas",
            "first_name": "Nicholas",
            "last_name": "Freemdom",
            "email": "nicholas@gmail.com",
            "password": "@password!",
            "is_active": True
        }
        User.objects.create_user(**self.data)
        self.user_list_url = reverse('user:user-list')
        self.user_detail_url = reverse('user:user-detail', args=[1])

    def test_list_user_success_response(self):
        response = self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, 200)

    def test_detail_user_success_response(self):
        response = self.client.get(self.user_detail_url)
        self.assertEqual(response.status_code, 200)

    def test_detail_user_fail_response(self):
        # Not found user
        url = reverse('user:user-detail', args=[5])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

