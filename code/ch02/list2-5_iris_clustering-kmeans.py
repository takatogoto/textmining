# -*- coding: utf-8 -*-
# リスト2-5 　scikit-learn を使って iris データを取り込み、散布図を描くプログラム例
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd
iris = load_iris()
species = ['Setosa','Versicolour', 'Virginica']
irispddata = pd.DataFrame(iris.data, columns=iris.feature_names)
irispdtarget = pd.DataFrame(iris.target, columns=['target'])

kmeans = KMeans(n_clusters=3).fit(irispddata)

irispd = pd.concat([irispddata, irispdtarget], axis=1)
iriskmeans = pd.concat([irispd, pd.DataFrame(kmeans.labels_, \
                        columns=['kmeans'])], axis=1)
irispd0 = iriskmeans[iriskmeans.kmeans == 0]
irispd1 = iriskmeans[iriskmeans.kmeans == 1]
irispd2 = iriskmeans[iriskmeans.kmeans == 2]

plt.scatter(irispd0['petal length (cm)'], irispd0['petal width (cm)'], c='red', \
            marker='x')
plt.scatter(irispd1['petal length (cm)'], irispd1['petal width (cm)'], c='blue', \
            marker='.')
plt.scatter(irispd2['petal length (cm)'], irispd2['petal width (cm)'], c='green', \
            marker='+')

plt.title('iris散布図、k-means法')
plt.xlabel('花弁の長さ(cm)')
plt.ylabel('花弁の幅(cm)')
plt.show()
