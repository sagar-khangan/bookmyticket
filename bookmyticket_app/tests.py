from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class BookMyTicketTests(APITestCase):

    def test_heath(self):
        url = reverse('health')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['status'],'success')

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('signup')
        data = {'username': 'test', 'email': 'test@email.com', 'password': 'test1231231'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test')

    def test_login(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('signup')
        data = {'username': 'test', 'email': 'test@email.com', 'password': 'test1231231'}
        response = self.client.post(url, data, format='json')
        url = reverse('get_auth_token')
        data = {'username': 'test', 'password': 'test1231231'}
        response = self.client.post(url, data, format='json')
        self.assertTrue('token' in response.data.keys())
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test')

    def test_login_failed(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('signup')
        data = {'username': 'test', 'email': 'test@email.com', 'password': 'test1231231'}
        response = self.client.post(url, data, format='json')
        url = reverse('get_auth_token')
        data = {'username': 'test', 'password': '123123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.get().username, 'test')

    def test_movie_booking_without_token_fail(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('book_movie')
        data = {
            "movie_show": 2,
            "seat_count": 1,
            "amount": 120,
            "seat": 3
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
