# -*- coding: utf-8 -*-
# 2.4.1節  数値計算ライブラリ NumPy
import numpy

na = numpy.array( [[1, 3, 5], [2, 4, 6]] )    # NumPyの配列に変換する
nb = numpy.array( [[1, 4, 7], [10, 13, 16]] )
print(na + nb)             # 配列naとnbの和
print(na * nb)             # 配列naとnbの要素ごとの積
print(na.dot(nb.T))          # 配列naに配列nbを掛ける（行列の積）
#print(numpy.dot(na, nb.T))   # 同上
print(na[1, 2])
print("SHAPE")
print(na.shape)
print("RESHAPE")
print(na.reshape(3,2))
print(na.T)

a = numpy.array([[1., 3.], [2., 4.]])
print(numpy.linalg.inv(a)) # 逆行列
                    #   array([[-2. ,  1.5],
                    #          [ 1. , -0.5]])
y = numpy.array([[5.],[7.]])
print(numpy.linalg.solve(a, y))  # 方程式 y = axを解く
                    #   array([[ 0.5],
                    #          [ 1.5]])
