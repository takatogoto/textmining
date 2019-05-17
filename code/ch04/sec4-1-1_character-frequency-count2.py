# -*- coding: utf-8 -*-
# 4.1.1 文字の出現頻度を数えるには
from collections import Counter
string = "吾輩は猫である。名前はまだ無い。"
cnt = Counter(string)
print(cnt)
