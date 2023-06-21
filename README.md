# Relative-Strength-calc

このプロジェクトでは、JPXが公開している東証上場銘柄一覧(`https://www.jpx.co.jp/markets/statistics-equities/misc/01.html`)を利用して、yahoo finance APIで株価を取得します。
以下の記事を参考にしています。
`https://myfrankblog.com/calculating_relative_strength/`

## 使用方法

1. `main.py`を実行します。
2. `get_stock_prices.py`が実行され、株価の取得が始まります。
取得中にエラーが発生した場合は、5秒後に最大2回まで再実行されます。当日のデータが取得できない場合、前日のデータを取得します。
取得に失敗した場合は値にNaNを挿入し、RS値は1として保存されます。
5000ほどの銘柄を取得するには数時間かかります。
処理が終わると`stock_prices.xlsx`に結果が保存されます。
3. `calculate_rs.py`が実行され、株価からRS値を計算します。
このプログラムではRSの計算方法に
`((((C - C63) / C63) * .4) + (((C - C126) / C126) * .2) + (((C - C189) / C189) * .2) + (((C - C252) / C252) * .2)) * 100`を採用しています。
Cは現在の株価、C63は63営業日前の株価を表します。
計算方法を変更したい場合は24行目のコードを書き換えてください。
処理が終わると`RS_calc.xlsx`に結果が保存されます。

## インストール
python 3.10.6で動作確認。

このプロジェクトを実行するには、以下のPythonパッケージが必要です。

- pandas
- numpy
- openpyxl
- yfinance
- tqdm

ターミナルで以下のコマンドを実行してください
- pip install -r requirements.txt


## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は`LICENSE`ファイルを参照してください。

## 変更履歴
`CHANGELOG.md`を参照してください