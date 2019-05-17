# -*- coding: utf-8 -*-
# リスト 4-2 文書全体を単語に分解し、出現頻度を数えるプログラム例
from collections import Counter
from aozora import Aozora
import MeCab
 
aozora = Aozora("wagahaiwa_nekodearu.txt")
string = '\n'.join(aozora.read())     # 1つの文字列データにする
 
# 形態素解析して、語の出現頻度を数える
m = MeCab.Tagger("-Ochasen")          # MeCabで単語に分割する
mecablist = []
wlist = m.parse(string).splitlines()  # 結果を単語情報リストのリストに整形する
for u in wlist:
    xlist = []
    for v in u.split():
       xlist.append(v)
    mecablist.append(xlist)

# 得られた単語情報リストのリストから、単語の部分だけを取り出したリストを作る
wordbodylist = []
for u in mecablist:
    wordbodylist.append(u[0])
# 単語のリストで出現頻度を数える
cnt = Counter(wordbodylist)
# 頻度順に100個表示
print(sorted(cnt.items(), key=lambda x: x[1], reverse=True)[:100])
