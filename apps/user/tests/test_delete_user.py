from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse


class DeleteUserTests(APITestCase):
    def setUp(self):
        User.objects.create_user(
            username='Nick',
            last_name='Freeman',
            email='nick@gmail.com',
            password='password',
            is_active=True
        )

    def test_delete_user_success_response(self):
        url = reverse('user:user-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_delete_user_fail_response(self):
        # Not found user
        url = reverse('user:user-detail', args=[2])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 404)
