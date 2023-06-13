import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import time
from tqdm import tqdm


url = "https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls"

# ExcelファイルをPandasデータフレームに読み込む
df = pd.read_excel(url)


# 空のデータフレームを作成
stock_df = pd.DataFrame(columns=["現在", "63日前", "126日前", "189日前", "252日前"])

# 各企業のコードと名前についてループ（プログレスバー付き）
for code, name in tqdm(zip(df['コード'], df['銘柄名']), total=len(df)):
    # コードを文字列に変換し、必要に応じてゼロを前に追加
    code_str = str(code).zfill(4)
    # Yahoo Financeの形式に合わせる
    ticker = f'{code_str}.T'

    # 株価を格納するリスト
    stock_prices = []

    # 指定された日数前の株価を取得
    for days_ago in [0, 63, 126, 189, 252]:
        # 取得する日付を計算
        date = datetime.now() - timedelta(days=days_ago)

        # 株価データを取得、失敗した場合は再試行する
        for _ in range(2):  # 最大2回試行
            data = yf.download(ticker, start=date,end=date + timedelta(days=1))
            if not data.empty:  # データが存在する場合はループを抜ける
                break
            time.sleep(5)  # 5秒待機してから再試行

        # 株価をリストに追加（データがない場合はNaNを追加）
        stock_prices.append(
            data['Close'][0] if not data.empty else float('nan'))

    # データフレームに株価を追加
    stock_df.loc[name] = stock_prices


# データフレームをExcelファイルに保存
stock_df.to_excel('stock_prices.xlsx')
print("株価をstock_prices.xlsxに保存しました")
