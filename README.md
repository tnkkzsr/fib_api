# フィボナッチ数を返すAPIサービス

## 概要
指定したn番目のフィボナッチ数を返すREST APIです。

使用言語/フレームワーク：Python3/Django

デプロイ環境：heroku

## エンドポイントURL
https://kazufib-fef02dd1ab53.herokuapp.com/fib

## Githubリポジトリ

https://github.com/tnkkzsr/fib_api

## ソースコードの構成

- 主な作業フォルダ：fib
- プロジェクトフォルダ(settings.pyなど)：fib_api 
- 主な処理：fib/views.py
- テストコード：fib/tests.py
- フィボナッチ数列に関するコード：fib/fib_calucurate.py


## 工夫点

### n番目のフィボナッチ数を返す関数の効率化
初めは再帰的にfib関数を呼び出すアルゴリズムを実装したが、n=99で試したところ計算がなかなか終わらなかった。反復法を用いることで計算量が減りnが増えても計算が比較的すぐ終わるようになった。
###  エラー処理の一般化
エラー処理を書く際、エラーメッセージ以外は同じようなコードになるので、エラーメッセージを返す部分を関数化してコードを整理した。


