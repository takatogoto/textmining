# -*- coding: utf-8 -*-
# 4.1.2 テキストを文ごとに分割し文字数を数える  文への分割
import nltk
from nltk.corpus import inaugural
text = inaugural.raw('1789-Washington.txt')
sents = nltk.tokenize.sent_tokenize(text)
for u in sents:
    print('>'+u+'<')
