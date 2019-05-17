# -*- coding: utf-8 -*-
# リスト 5-15　 安倍首相所信表明演説の段落間LSI類似度をグラフと樹形図に表示するプログラム例
import numpy as np
import re, itertools, MeCab
from collections import defaultdict
from gensim import corpora, models, similarities
from pprint import pprint
from igraph import *
def readin(filename):
    with open(filename, "r") as afile:
        whole_str = afile.read()
    sentenses = (re.sub('。', '', whole_str)).splitlines()
    return [re.sub('　', '', u) for u in sentenses if len(u)!=0]
num_topics = 10
m = MeCab.Tagger("-Ochasen")  # MeCabで品詞分解する
filename = "abe.txt"
string = readin(filename)
# 文単位で形態素解析し、基本形を文ごとのリストにする
sentensewordlist = [ \
    [v.split()[2] for v in m.parse(sentense).splitlines()  \
    if (len(v.split()) >=3 and v.split()[3][:2] in ['名詞','動詞','形容詞', \
                                                    '形容動詞','副詞'])] \
    for sentense in string]
# 各パラグラフの先頭文字（図でパラグラフを示すときに使う）
headlist = [ \
    sentense[2:6] if sentense[0] in ['一', '二', '三', '四', '五', '六', '七', '八', \
                                     '九', '十'] else 
    sentense[1:5] if sentense[0] in ['　', '（', '「'] else sentense[:4] \
       for sentense in string]
stoplist = {'が', 'は', 'に', 'も', 'の', 'を', 'へ', 'と', 'で', 'や', 'ば', \
 'だ', 'て', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十', \
 '〇', '（', '）', '＊', '「', '」', '、', '。', 'ます', 'ある', 'こと', 'する', \
 'など', 'です', 'た', 'たち', 'その', '的', 'ため', 'いる', 'できる', 'れる', \
 'これ', 'なる', '化', ')', '(', '年', '円', '万'}
# stoplistに含まれる語を取り除く
texts = [[word for word in doc if word not in stoplist] for doc in \
         sentensewordlist]
# N回以上現れる語のみを拾う
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
texts = [[token for token in text if frequency[token] >= 3] for text in texts]

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
# TF-IDFの計算
tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model
corpus_tfidf = tfidf[corpus]
# LSIモデルクラスのインスタンス生成。corpus_tfidfを入力、トピック数をnum_topicsに設定
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topics)
corpus_lsi = lsi[corpus_tfidf] # corpus_tfidfを処理
ttlist = []
# lsi.show_topicsの出力を整形して表示
for t in lsi.show_topics(num_topics, formatted=False):
    tnum = t[0]
    tlist = sorted(t[1], key=lambda u: u[1], reverse=True)[:3]
    ttlist.append( [u[0] for u in tlist] )
    print(tnum, end='  ')
    for u in tlist:   print(u[0], "%.4f" % u[1], end='   ')
    print()
# corpus_lsiの内容を整形して表示
for i, doc in enumerate(corpus_lsi):
    x = [ sorted(doc, key=lambda u: u[1], reverse=True) for u in doc if len(u)!=0]
    if len(x)!=0:
        print(headlist[i], end='  ')  # 段落番号の代わりにheadlistを使って表示
        for u in x[0][:3]:
            if (u[1] >= 0.1):
                print(ttlist[u[0]], np.round(u[1],3), end=' ')
        print()
    print('---')
# lsi[corpus]の類似度を計算
index = similarities.MatrixSimilarity(lsi[corpus]) 
# 類似度を行列に成形
simmatrix = []
for doc in texts:
    doc = ' '.join(doc)
    vec_bow = dictionary.doc2bow(doc.split())
    vec_lsi = lsi[vec_bow]  # convert the query to LSI space
    sims = index[vec_lsi]   # 元のコーパスの文に対して類似度を計算
    simmatrix.append(sims)

# igraphによるグラフ化
minsim = 0.85
edges = []
vertices = headlist         # グラフの頂点はheadlistの文字列
for i, u in enumerate(simmatrix):
    for j, v in enumerate(u):
        if v >= minsim and i!=j:  # 値がminsim以上で、対角要素でなければ、辺行列に入れる
            edges.append([i, j])
g = Graph(vertex_attrs={"label": vertices}, edges=edges, directed=False)
plot(g, vertex_size=35, vertex_label_size=9, bbox=(800,800), vertex_color='white')

# 類似度マトリックス（＝距離マトリックス）からデンドログラムへ出力
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
Z = linkage(simmatrix, 'ward')  # Ward法で階層化クラスタリング
dendrogram(                     # デンドログラムを描く
    Z,
    leaf_rotation=90.,          # x軸ラベルを90度回転
    leaf_font_size=8.,          # x軸ラベルのフォントを8ポイントにする
    labels=np.array(headlist),  # データラベルをheadlistから引用
)
plt.show()
