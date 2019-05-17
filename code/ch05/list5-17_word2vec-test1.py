# -*- coding: utf-8 -*-
# リスト 5-17 Word2Vec の利用フェーズのプログラム例 1   単純な利用
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', \
                    level=logging.INFO)

model = gensim.models.word2vec.Word2Vec.load("jpwmodel")
print("model load complete")

# similarityチェック
print(model.most_similar(positive=[u'女性', u'王'], negative=[u'男性'], topn=5))
print(model.most_similar(positive=[u'パリ', u'フランス'], \
                         negative=[u'ベルリン'], topn=5))
print(model.similarity(u'ロンドン', u'東京'))

# 登録されている語のリストを取り出す
voc = model.vocab.keys()
# 語xのベクトルを取り出す。語が登録されていないとKeyError例外を返す
x = '東京'
wvec = model[x]
