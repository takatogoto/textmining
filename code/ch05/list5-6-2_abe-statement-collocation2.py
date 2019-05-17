# -*- coding: utf-8 -*-
# リスト 5-6(2) 施政方針演説のネットワークの構造を分析する例
import re
import numpy as np
from collections import Counter
import MeCab
import itertools
from igraph import *
from aozora import Aozora
minfreq = 0                   # グラフ描画のときは4に設定し、見やすくする
m = MeCab.Tagger("-Ochasen")  # MeCabで品詞分解する
 
def readin(filename):
    with open(filename, "r") as afile:
        whole_str = afile.read()
    sentenses = (re.sub('。', '。\n', whole_str)).splitlines()
    return [re.sub('　', '', u) for u in sentenses if len(u)!=0]
 
filename = "abe.txt"
string = readin(filename)
 
# 文単位で形態素解析し、名詞だけ抽出し、基本形を文ごとのリストにする
sentensemeishilist = [ \
    [v.split()[2] for v in m.parse(sentense).splitlines() \
       if (len(v.split())>=3 and v.split()[3][:2]=='名詞')] \
    for sentense in string]

# 文ごとにペアリストを作る
doubletslist = [ \
    list(itertools.combinations(meishilist,2)) \
       for meishilist in sentensemeishilist if len(meishilist) >=2 ]
alldoublets = []
for u in doubletslist:  # 文ごとのペアリストのリストをフラットなリストにする
    alldoublets.extend(u)
 
# 名詞ペアの頻度を数える
dcnt = Counter(alldoublets)
 
# 出現頻度順にソートした共起ペアを出力する（上位30ペア）
print('pair frequency', sorted(dcnt.items(), key=lambda x: x[1], \
      reverse=True)[:30])
    # 頻度順に表示
# 名詞ペアの頻度辞書から、頻度が4以上のエントリだけを抜き出した辞書を作る
restricteddcnt = dict( ( (k, dcnt[k]) for k in dcnt.keys() if dcnt[k]>=minfreq ) )
charedges = restricteddcnt.keys()
vertices = list(set( [v[0] for v in charedges] + [v[1] for v in charedges] ))
 
# charedgesは(['名詞','名詞'])の形なのでvertid(数字)ペア([1,3])に変換する
edges = [(vertices.index(u[0]), vertices.index(u[1])) for u in charedges]

g = Graph(vertex_attrs={"label": vertices, "name": vertices}, \
          edges=edges, directed=False)
plot(g, vertex_size=30, bbox=(800,800), vertex_color='white')

print('average path length', g.average_path_length())
print("path length hist\n", g.path_length_hist())

degreelist = zip(vertices, g.degree())
print(sorted(degreelist, key=lambda x: x[1], reverse=True)[:30])

print("eccentricity centrality", sorted( zip(vertices, [1/u for u in list(g.eccentricity())]), key=lambda x: x[1], reverse=True)[:30])
print("closeness",  sorted( zip(vertices, list(g.closeness())), key=lambda x: x[1], reverse=True)[:30] )

print("degree centrality", sorted( zip(vertices, [u/(len(g.degree())-1) for u in list(g.degree())]), key=lambda x: x[1], reverse=True)[:30])

print("eigenvalue-based centrality",  sorted( zip(vertices, list(g.evcent())), key=lambda x: x[1], reverse=True)[:30] )

print("betweenness",  sorted( zip(vertices, list(g.betweenness())), key=lambda x
: x[1], reverse=True)[:30] )

print('maximal cliques', \
  [ [vertices[v] for v in u] for u in list(g.maximal_cliques()) ] )
print('largest cliques', \
    [ [vertices[v] for v in u] for u in list(g.largest_cliques()) ] )

print('community info map', g.community_infomap())
plot(g.community_infomap(), vertex_size=30, bbox=(800,800), )
