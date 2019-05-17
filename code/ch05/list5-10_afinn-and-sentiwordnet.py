# -*- coding: utf-8 -*-
# リスト 5-10 SentiWordNet による単語の感情値の和を求めるプログラム例
from nltk.tokenize import *

AFINNfile = 'AFINN/AFINN-111.txt'
sentiment_dictionary = {}
for line in open(AFINNfile):  # AFINN-111辞書の読み込み
    word, score = line.split('\t')
    sentiment_dictionary[word] = int(score)

str = '''The first music is good, but the second and the third musics \
 are terrible and boring.  It is a bad idea to buy this CD.'''
for sent in sent_tokenize(str):
    words = word_tokenize(sent.lower())
    score = sum(sentiment_dictionary.get(word, 0) for word in words)
    print(score)

result = []
for sent in sent_tokenize(str):
    print(sent)
    words = word_tokenize(sent.lower())
    pos = 0
    neg = 0
    for word in words:
        score = sentiment_dictionary.get(word, 0)
        if score > 0:
            pos += score
        if score < 0:
            neg += score
    result.append([pos, neg])
for u in result:
    print(u)
