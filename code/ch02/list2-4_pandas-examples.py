# -*- coding: utf-8 -*-
# リスト2-4  pandas のデータフレームを使ったプログラム例
import pandas as pd
indata = [('Tronto', 175, 68, 25), ('Detroit', 183, 70, 23), ('Boise', 190, 72, 26)]
df = pd.DataFrame(data=indata, columns=['出生地', '身長', '体重', '年齢'], \
                  index=['Bill', 'John', 'Fred'])
print(df)
print(df['体重'])
print(df[['体重', '身長']])
print(df['体重']['John':'Fred'])
print(df['体重'][1:3])
print(df.ix[1,3])  # id=1, col=3を指定

print(df['体重'].sum())     # 合計。結果は210
print(df['体重'].mean())    # 算術平均。結果は70.0
print(df['体重'].median())  # 中央値。結果は70.0
print(df['体重'].max())     # 最大値。結果は72

from matplotlib import pyplot as plt
df['身長'].plot.bar()  # pandasのデータフレームのメソッドplot.barを使う
plt.show()

df = pd.read_excel('ファイル名', 'Sheet1')        # xlsxファイルのSheet1を読み込む場合
df = pd.read_csv('ファイル名', encoding='utf-8')  # CSVファイルを読み込む場合
df.to_excel('test.xlsx', 'シート名')            # xlsxファイルを書き出す場合
