# -*- coding: utf-8 -*-
# リスト2-3  Matplotlib を使った単純なプロットのプログラム例
import numpy as np
import matplotlib.pyplot as plt
 
t = np.arange(0., 5., 0.2)
plt.title('drawing example1')
# red dashes, blue squares and green triangles
 
plt.plot(t, t, 'r--', label='linear')    # y=xの直線。赤（r）でダッシュ（--）、名前はlinear
plt.plot(t, t**2, 'bs', label='square')  # y=x^2、青（b）で四角（s）、名前はsquare
plt.plot(t, t**3, 'g^', label='cube')    # y=x^3、緑（g）で三角（^）、名前はcube
plt.xlabel('x values')                   # x軸のタイトルはx values
plt.ylabel('y values')                   # y軸のタイトルはy values
plt.legend()                             # 凡例を書く
plt.show()                               # この絵を表示する
