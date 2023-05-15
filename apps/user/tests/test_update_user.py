from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse


class PatchUserTests(APITestCase):
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
        self.extra_data = {
            "username": "nicky",
            "first_name": "Nicky",
            "last_name": "Freeky",
            "email": "nicky_freeky@gmail.com"
        }
        User.objects.create_user(**self.data)
        self.url = reverse('user:user-detail', args=[1])

    def test_partial_update_user_success_response(self):
        data = {"email": "nick_freeman@gmail.com"}
        response = self.client.patch(self.url, data)
        self.assertEqual(response.status_code, 200)

    def test_partial_update_user_fail_response(self):
        # Not found user
        url = reverse('user:user-detail', args=[5])
        data = {"email": "nick@gmail.com"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 404)

        # Unique username constraint
        data = {"username": "nicholas"}
        response = self.client.patch(self.url, data)
        self.assertEqual(response.status_code, 400)

    def test_update_user_success_response(self):
        response = self.client.patch(self.url, self.extra_data)
        self.assertEqual(response.status_code, 200)

    def test_update_user_fail_response(self):
        # Not found user
        url = reverse('user:user-detail', args=[5])
        response = self.client.put(url, self.extra_data)
        self.assertEqual(response.status_code, 404)

        # Unique username constraint
        data = {
            "username": "nicholas",
            "first_name": "Nike",
            "last_name": "Freeze",
            "email": "nicholas_freeze@gmail.com"
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, 400)
