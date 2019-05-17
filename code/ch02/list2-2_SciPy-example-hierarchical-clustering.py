# -*- coding: utf-8 -*-
# リスト2-2  SciPy を使ったプログラム例    階層型クラスタリング
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
X = np.array([[1,2], [2,1], [3,4], [4,3]])
Z = linkage(X, 'ward')  # Ward法を使って階層型クラスタリングを行う
dendrogram(Z)           # 樹形図（dendrogram）を描く
plt.show()              # 図形を画面に描画する
