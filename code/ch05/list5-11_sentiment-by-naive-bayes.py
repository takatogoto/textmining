# -*- coding: utf-8 -*-
# リスト 5-11 機械学習を使った感情判定のプログラム例
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

def format_sentense(sentense):
    return {word: True for word in word_tokenize(sentense) }

pos_data = []
with open('rt-polaritydata/rt-polarity.pos', encoding='latin-1') as f:
    for line in f:
        pos_data.append([format_sentense(line), 'pos'])
neg_data = []
with open('rt-polaritydata/rt-polarity.neg', encoding='latin-1') as f:
    for line in f:
        neg_data.append([format_sentense(line), 'neg'])

# 学習データはそれぞれ前半4,000文ずつ
training_data = pos_data[:4000] + neg_data[:4000]
# 評価データはそれぞれ4,000以降の文
testing_data = pos_data[4000:] + neg_data[4000:]

# training_dataを使って分類気を作る
model = NaiveBayesClassifier.train(training_data)

s1 = 'This is a nice article'
s2 = 'This is a bad article'
print( s1, '--->', model.classify(format_sentense(s1)) )  # 2つの文例s1、s2で試す
print( s2, '--->', model.classify(format_sentense(s2)) )

print('accuracy', accuracy(model, testing_data))  # testing_dataを使って精度計算
