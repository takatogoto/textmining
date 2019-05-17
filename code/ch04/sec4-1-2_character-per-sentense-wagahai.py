# -*- coding: utf-8 -*-
# 4.1.2節 テキストを文ごとに分割し文字数を数える  文ごとの文字数分布の例
from collections import Counter
import re
import numpy as np
import matplotlib.pyplot as plt
from aozora import Aozora
 
aozora = Aozora("wagahaiwa_nekodearu.txt")
 
# 文に分解してから、文ごとに文字数をカウントする
string = '\n'.join(aozora.read())
# 全角空白を取り除く。句点・改行で分割、。」の。は改行しない
string = re.split('。(?!」)|\n', re.sub('　', '', string))
while '' in string:  string.remove('')   # 空行を除く
 
cnt = Counter([len(x) for x in string])  # stringの要素（文）の長さをリストにする
# 文の長さを頻度順にソートして出力する
print(sorted(cnt.items(), key=lambda x: x[1], reverse=True)[:100])

nstring = np.array([len(x) for x in string if len(x) < 150])
print('max', nstring.max())
plt.hist(nstring, bins=nstring.max())
plt.show()

print(sorted(cnt.items(), reverse=True)[:100])  # 文の長さを頻度順にソートして出力する

aozora = Aozora("hashire_merosu.txt")
# 文に分解してから、文ごとに文字数をカウントする
string = '\n'.join(aozora.read())
# 全角空白を取り除く。句点・改行で分割、。」の。は改行しない
string = re.split('。(?!」)|\n', re.sub('　', '', string))
while '' in string:  string.remove('')   # 空行を除く
 
cnt = Counter([len(x) for x in string])  # stringの要素（文）の長さをリストにする
# 文の長さを頻度順にソートして出力する
print(sorted(cnt.items(), key=lambda x: x[1], reverse=True)[:100])

nstring = np.array([len(x) for x in string if len(x) < 150])
print('max', nstring.max())
plt.hist(nstring, bins=nstring.max())
plt.title('『我輩は猫である』文ごとの文字数分布')
plt.xlabel('文の文字数')
plt.ylabel('出現頻度')
plt.show()
