import pandas as pd
import numpy as np

def calculate_rs():

    # Excelファイルからデータを読み込む
    df = pd.read_excel('stock_prices.xlsx', index_col=0)

    # RS値を計算するための空のリストを作成
    rs_values = []

    # 各行（企業）についてループ
    for index, row in df.iterrows():
        # 各要素を変数に代入
        current_price = row['現在']
        price_63_days_ago = row['63日前']
        price_126_days_ago = row['126日前']
        price_189_days_ago = row['189日前']
        price_252_days_ago = row['252日前']

        # NaNが含まれる場合はRS値を1とする
        if pd.isnull(current_price) or pd.isnull(price_63_days_ago) or pd.isnull(price_126_days_ago) or pd.isnull(price_189_days_ago) or pd.isnull(price_252_days_ago):
            rs = 1
        else:
            # RS値を計算
            rs = ((((current_price - price_63_days_ago) / price_63_days_ago) * .4) +
                (((current_price - price_126_days_ago) / price_126_days_ago) * .2) +
                (((current_price - price_189_days_ago) / price_189_days_ago) * .2) +
                (((current_price - price_252_days_ago) / price_252_days_ago) * .2)) * 100

        # RS値をリストに追加
        rs_values.append(rs)

    # RS値をデータフレームに追加
    df['RS'] = rs_values

    # RS値を降順に並び替え
    df = df.sort_values('RS', ascending=False)

    # 素点を計算
    df['素点'] = np.floor(100 - np.arange(len(df)) / len(df) * 100)

    # データフレームをExcelファイルに保存
    df.to_excel('RS_calc.xlsx')

    print("RS_calc.xlsxとして保存しました")
