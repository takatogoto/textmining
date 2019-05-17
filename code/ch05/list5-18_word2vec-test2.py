# -*- coding: utf-8 -*-
# リスト 5-18  Word2Vec の利用フェーズのプログラム例 2    scikit-learn とあわせて単語をクラスタリングする
import gensim, logging
import scipy.spatial.distance
import scipy.cluster.hierarchy
import matplotlib
from matplotlib.pyplot import show
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', \
                    level=logging.INFO)

model = gensim.models.word2vec.Word2Vec.load("jpw-wakati-model")
print("model load complete")

wv = []
vocnew = []
voc = [u'ビール', u'日本酒', u'焼酎', u'蕎麦', u'スパゲッティ', 
    u'ハンバーグ', u'カレー', u'バラ', u'桜']
for x in voc:
    try:
        wv.append(model[x])
    except KeyError:
        print(x, u'を無視します')
    vocnew.append(x)

# linkage配列を作る
l = scipy.cluster.hierarchy.linkage(wv, method='average')  # method='ward'でもよい
# lをdentrogramに表現する
scipy.cluster.hierarchy.dendrogram(l, labels=vocnew)
show()
