from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TestView(APIView):
    def get(self, request):
        return Response({"message": "ok"}, 200)


def fib(n):
    if n <= 1:
            return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

class FibView(APIView):
    def get(self,request):

        n = request.GET.get("n")

        #クエリパラメータに何もない時
        if n is None:
            return Response({
                "status":400,
                "error":"クエリパラメータが空です。数字を入力してください",
                },status=status.HTTP_400_BAD_REQUEST)
        #クエリパラメータが数字(10進数)でない時
        if not n.isdecimal():
            return Response({
                "status":400,
                "error":"クエリパラメータには正の整数を入力してください"
                },
                status=status.HTTP_400_BAD_REQUEST)
        
        n = int(n)

        #クエリパラメータが0以下の数字の時
        if n <= 0:
            return Response({"error":"Please provide a positive number"},status=status.HTTP_400_BAD_REQUEST)
        

        return Response({"result":fib(n)})

