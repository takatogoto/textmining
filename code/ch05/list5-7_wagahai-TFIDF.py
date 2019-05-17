# -*- coding: utf-8 -*-
# リスト 5-7 『吾輩は猫である』の先頭 3 文の TF-IDF を求めるプログラム例
import re
import numpy as np
import MeCab
from aozora import Aozora
from sklearn.feature_extraction.text import TfidfVectorizer
aozora = Aozora("wagahaiwa_nekodearu.txt")

# 文に分解する
string = '\n'.join(aozora.read())
string = re.sub('　', '', string)
string = re.split('。(?!」)|\n', re.sub('　', '', string))
while '' in string:  string.remove('')  # 空行を除く
m = MeCab.Tagger("-Owakati")            # MeCabで分かち書きにする
wakatilist = []
for sentense in string:
    # 文末に挿入される改行をrstripで除去する
    wakatilist.append(m.parse(sentense).rstrip())

wakatilist = np.array(wakatilist)  # scikit-learnの入力とするためにNumPyのnarrayに変換
wakatilist = wakatilist[3:6]       # 先頭の3行分だけを入力にする

vectorizer = TfidfVectorizer(use_idf=True, norm=None, \
                             token_pattern=u'(?u)\\b\\w+\\b')
   # norm=Noneは、出力を行ごとのベクトルと見たときに長さを1にする（正規化）処理をしないように指定
tfidf = vectorizer.fit_transform(wakatilist)
print(tfidf.toarray())             # 出力を表示
