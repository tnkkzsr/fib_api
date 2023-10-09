# フィボナッチ数列を返すAPIビューを定義するファイル
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .fib_calucurate import fib
from django.http import JsonResponse

#クエリパラメータの最大値。これを超えるとエラーを返す
MAX_N = 20577 

error_messages = {
    "none_request":"クエリパラメータnが空です。https://kazufib-fef02dd1ab53.herokuapp.com/fib/?n=⚪︎に正の整数を入力してください",
    "not_number_request":"クエリパラメータnが整数ではありません。クエリパラメータには正の整数を入力してください",
    "negative_number_request":"クエリパラメータnが正の数ではありません。クエリパラメータには正の整数を入力してください。",
    "over_max_n_request":"クエリパラメータnが大きすぎます。クエリパラメータには20577以下の正の整数を入力してください",
}

#エラーメッセージを返す関数
def error_response(error_message):
    return Response({
        "status": status.HTTP_400_BAD_REQUEST,
        "error": error_message
    }, status=status.HTTP_400_BAD_REQUEST)

#フィボナッチ数列を返すAPIビュー
class FibView(APIView):

    def get(self,request):

        n = request.GET.get("n")

        #クエリパラメータに何もない時
        if n is None:
            return error_response(error_messages["none_request"])
                
        try:
            n = int(n)
        except ValueError: #クエリパラメータが整数ではない時
            if n == "":
                return error_response(error_messages["none_request"])
            return error_response(error_messages["not_number_request"])

        if n > MAX_N: #クエリパラメータが20577より大きい時
            return error_response(error_messages["over_max_n_request"])

        # クエリパラメータが0以下の数字の時
        if n <= 0:
            return error_response(error_messages["negative_number_request"])

        return Response({"result":fib(n)})

#404エラーを返すビュー
def custom_404(request, exception):
    data = {
        'status': 404,
        'error':"Not Found"
    }
    return JsonResponse(data, status=404)
