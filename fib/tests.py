from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class TestFibView(APITestCase):

    def test_none_request(self):
        url = reverse("fib")
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"],"クエリパラメータnが空です。https://kazufib-fef02dd1ab53.herokuapp.com/fib/?n=⚪︎に正の整数を入力してください")

    def test_not_number_request(self):
        url = reverse("fib") + "?n=abc"
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"],"クエリパラメータnが整数ではありません。クエリパラメータには正の整数を入力してください")

    def test_negative_number_request(self):
        url = reverse("fib") + "?n="+str(-1)
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"],"クエリパラメータnが正の数ではありません。クエリパラメータには正の整数を入力してください。")

    def test_valied_get_request(self):
        url = reverse("fib") + "?n=10"
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data["result"],55)

    def test_over_max_n_request(self):
        url = reverse("fib") + "?n=20578"
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"],"クエリパラメータnが大きすぎます。クエリパラメータには20577以下の正の整数を入力してください")
