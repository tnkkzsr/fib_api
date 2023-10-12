# フィボナッチ数を返すAPIサービス

## 概要
指定したn番目のフィボナッチ数を返すREST APIです。

使用言語/フレームワーク：Python3/Django

デプロイ環境：heroku

## エンドポイントURL
https://kazufib-fef02dd1ab53.herokuapp.com/fib


## ソースコードの構成

- 主な作業フォルダ：fib
- プロジェクトフォルダ(settings.pyなど)：fib_api 
- 主な処理：fib/views.py
- テストコード：fib/tests.py
- フィボナッチ数列に関するコード：fib/fib_calucurate.py


## 工夫点

### n番目のフィボナッチ数を返す関数の効率化
初めは再帰的にfib関数を呼び出すアルゴリズムを実装したが、n=99で試したところ計算がなかなか終わらなかった。反復法を用いることで計算量が減りnが増えても計算が比較的すぐ終わるようになりました。
###  エラー処理の一般化
エラー処理を書く際、エラーメッセージ以外は同じようなコードになるので、エラーメッセージを返す部分を関数化してコードを整理しました。

## エラー処理
このAPIは、以下のエラー処理を行っています。

1. クエリパラメータが存在しない場合

2. クエリパラメータが整数ではない場合

3. クエリパラメータが0以下の場合

4. クエリパラメータが大きすぎる時

5. ページが見つからない場合


## テストの実行結果


```bash
python manage.py test

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
......
----------------------------------------------------------------------
Ran 6 tests in 0.013s

OK
Destroying test database for alias 'default'...
