
#n番目のフィボナッチ数を返す関数
def fib(n):
    if n <= 1:
            return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# エラーが出てくるnの上限値を調べる関数
# 結果20578でエラーが出ることがわかった
def limit_test_fib():
    for i in range(1, 100000): 
            try:
                result = fib(i)
                print(f"n={i}, fib={result}")
            except Exception as e:
                print(f"Error at n={i}: {e}")
                break