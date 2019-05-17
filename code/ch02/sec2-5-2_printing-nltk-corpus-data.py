# -*- coding: utf-8 -*-
# 2.5.2節  NLTK に含まれるコーパスデータ　　NTLKのデータを表示する
from nltk.book import *
for u in text7:
    print(u, end=' ')
    if u=='.':
        print()
