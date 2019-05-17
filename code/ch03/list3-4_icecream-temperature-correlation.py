# -*- coding: utf-8 -*-
# リスト 3-4 アイスクリームの売上と気温から相関係数・回帰方程式を求めるプログラム例
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm  # 回帰分析はstatsmodelsパッケージを利用する

# 2016年　一世帯当たりアイスクリーム支出金額　　一般社団法人日本アイスクリーム協会
# https://www.icecream.or.jp/data/expenditures.html

icecream = [[1,464],[2,397],[3,493],[4,617],[5,890],[6,883],[7,1292], \
   [8,1387],[9,843],[10,621],[11,459],[12,561]]

# 2016年　月別平均気温　気象庁　http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3.php?
# prec_no=44&block_no=47662&view=a2

temperature = [[1,10.6],[2,12.2],[3,14.9],[4,20.3],[5,25.2],[6,26.3], \
   [7,29.7],[8,31.6],[9,27.7],[10,22.6],[11,15.5],[12,13.8]]

x = np.array([u[1] for u in temperature])
y = np.array([u[1] for u in icecream])
X = np.column_stack((np.repeat(1, x.size), x) )
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())
b, a = results.params  # statsmodelsのOLSではb, aの順で返される
print('a', a, 'b', b)
print('correlation coefficient', np.corrcoef(x, y)[0,1])
# グラフを描く
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x, y)
ax.plot(x, a*x+b)
plt.title('2016年の気温と一世帯当たりアイスクリーム売上')
plt.xlabel('月間平均気温（℃）')
plt.ylabel('月間アイスクリーム売上げ（円）')
plt.show()
