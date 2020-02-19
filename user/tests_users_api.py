from django.test import TestCase
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.

CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    user = User(**params)
    user.save()
    return user


class PublicApiTest(TestCase):
    ''' Test the API user public '''

    def setup(self):
        self.client = APIClient()

    def test_created_valid_user(self):
        payload = {"username": "djangoTest",
                   "email": "anwar@test.com",
                   "password": "test123"
                   }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exits(self):
        payload = {"username": "exist",
                   "email": "exist@test.com",
                   "password": "exist123",
                   }

        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_passwors_too_short(self):
        payload = {'username': 'passtest',
                   'password': 'abi',
                   'email': 'pass@test.com'
                   }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        user_exists = User.objects.filter(
            username=payload['username']).exists()
        self.assertFalse(user_exists)
