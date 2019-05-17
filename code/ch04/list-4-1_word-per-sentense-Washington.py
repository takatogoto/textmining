# -*- coding: utf-8 -*-
# リスト 4-1 文に分割し、さらに単語に分割して数える例
import matplotlib.pyplot as plt
import numpy as np
import nltk
from nltk.corpus import inaugural
from collections import Counter
sents = nltk.tokenize.sent_tokenize(inaugural.raw('1789-Washington.txt'))
 
cnt = Counter(len(sent.split()) for sent in sents)
print(sorted(cnt.items(), key=lambda x: [x[1], x[0]], reverse=True))
 
nstring = np.array( [len(sent.split()) for sent in sents] )
plt.hist(nstring)
plt.title('1789年ワシントン就任演説の文ごとの単語数分布')
plt.xlabel('文の単語数')
plt.ylabel('出現頻度')
plt.show()
