# -*- coding: utf-8 -*-
# 4.2.2節　日本語の単語の出現頻度の分析　MeCabの使い方
import MeCab
string = '吾輩は猫である。'
m = MeCab.Tagger("-Ochasen")      # MeCabのインスタンスを作りmとする
out = m.parse(string)             # 入力stringをm.parseで分解する
print(out)
xlist = [u.split() for u in m.parse(string).splitlines()]
print(xlist)
