# -*- coding: utf-8 -*-
# 2.3.5 内包 --- enumerate や zip　　内包による処理速度アップ
import time
def sample_loop(n):           # for loopを使った場合
    r = []
    for i in range(n):
        r.append(i)
    return r
def sample_comprehension(n):  # リスト内包を使った場合
    return [i for i in range(n)]

start = time.time()
sample_loop(10000)
print(time.time() - start, 'sec')
start = time.time()
sample_comprehension(10000)
print(time.time() - start, 'sec')
