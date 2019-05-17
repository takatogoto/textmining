# -*- coding: utf-8 -*-
# 2.3.1節  Python プログラムの構造  ブロック構造は段下げで表す  関数の定義をする最初の部分
import math

def newfunction(x):
    y = math.sin(x) + 1
    return y**x

print newfunction(0.5)
