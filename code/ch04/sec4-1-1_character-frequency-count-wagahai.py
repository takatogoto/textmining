# -*- coding: utf-8 -*-
# 4.1.1節 文字の出現頻度  青空文庫のテキストを取り込んで、文字の出現回数を数える
from collections import Counter
from aozora import Aozora
aozora = Aozora("wagahaiwa_nekodearu.txt")
 
# 文字ごとの出現頻度を調べる
string = '\n'.join(aozora.read())  # パラグラフをすべて結合して1つの文字列にする
cnt = Counter(string)
# 頻度順にソートして出力する
print(sorted(cnt.items(), key=lambda x: x[1], reverse=True)[:50])
