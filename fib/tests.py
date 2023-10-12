from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .fib_calucurate import fib

class TestFibView(APITestCase):

    def test_none_request(self):
        url = reverse("fib")
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["error"],"クエリパラメータnが空です。https://kazufib-fef02dd1ab53.herokuapp.com/fib?n=⚪︎に正の整数を入力してください")

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


class Custom404TestCase(TestCase):
    
    def test_custom_404_response(self):
    
        response = self.client.get(reverse('fib') + 'nonexistent/')
        self.assertEqual(response.status_code, 404)
        expected_data = {
            'status': 404,
            'error': 'Not Found'
        }
        self.assertJSONEqual(response.content, expected_data)


def test_fib():
    # 基本的なテスト
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8

    # 適当な値のテスト
    assert fib(100) == 354224848179261915075
    assert fib(500) == 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
    assert fib(1000) == 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
