from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class TestFibView(APITestCase):

    def test_none_request(self):
        url = reverse("fib")
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"],"Please provide a number")

    def test_not_number_request(self):
        url = reverse("fib") + "?n=abc"
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"],"Please provide a number")

    def test_negative_number_request(self):
        url = reverse("fib") + "?n=-1"
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"],"Please provide a positive number")

    def test_valied_get_request(self):
        url = reverse("fib") + "?n=10"
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data["result"],55)
