# -*- coding: utf-8 -*-
# リスト2-6  StatsModels を使って相関係数を計算するプログラム例
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm  # 回帰分析はstatsmodelsパッケージを利用する
icecream = [[1,464],[2,397],[3,493],[4,617],[5,890],[6,883],
       [7,1292],[8,1387],[9,843],[10,621],[11,459],[12,561]]
temperature = [[1,10.6],[2,12.2],[3,14.9],[4,20.3],[5,25.2],
       [6,26.3],[7,29.7],[8,31.6],[9,27.7],[10,22.6],[11,15.5],[12,13.8]]

x = np.array([u[1] for u in temperature])
y = np.array([u[1] for u in icecream])
X = np.column_stack((np.repeat(1, x.size), x))
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())
b, a = results.params
print('a', a, 'b', b)
print('correlation coefficient', np.corrcoef(x, y)[0,1])
