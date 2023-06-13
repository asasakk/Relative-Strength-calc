import subprocess


print("株価を取得するプログラムを実行します。")

# 株価を取得するプログラムを実行
subprocess.run(["python", "get_stock_prices.py"])

print("取得した株価からRS値を計算するプログラムを実行します。")

# RSを計算するプログラムを実行
subprocess.run(["python", "calculate_rs.py"])
