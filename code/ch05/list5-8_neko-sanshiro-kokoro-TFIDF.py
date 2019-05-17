# -*- coding: utf-8 -*-
# リスト 5-8  『吾輩は猫である』『三四郎』『こころ』の TF-IDF を計算するプログラム例
import numpy as np
import pandas as pd
import MeCab
from aozora import Aozora
from sklearn.feature_extraction.text import TfidfVectorizer
#
aozoradir = "./"
m = MeCab.Tagger("-Owakati")  # MeCabで分かち書きにする

files = ['wagahaiwa_nekodearu.txt', 'sanshiro.txt', 'kokoro.txt']
readtextlist = [Aozora(aozoradir + u) for u in files]
stringlist = ['\n'.join(u.read()) for u in readtextlist]
wakatilist = [m.parse(u).rstrip() for u in stringlist]
wakatilist = np.array(wakatilist)

# norm=Noneでベクトルの正規化（長さを1にする）をやめる
vectorizer = TfidfVectorizer(use_idf=True, norm=None, \
                             token_pattern=u'(?u)\\b\\w+\\b')

tfidf = vectorizer.fit_transform(wakatilist)
tfidfpd = pd.DataFrame(tfidf.toarray())     # pandasのデータフレームに変換する
itemlist = sorted(vectorizer.vocabulary_.items(), key=lambda x:x[1])
tfidfpd.columns = [u[0] for u in itemlist]  # 欄の見出し（単語）を付ける

for u in tfidfpd.index:
   print(tfidfpd.T.sort_values(by=u, ascending=False).iloc[:50 ,u])
   # 行と列を転置したものを、それぞれの文書に対して降順にソートし、先頭50語を表示
