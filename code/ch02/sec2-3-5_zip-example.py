# -*- coding: utf-8 -*-
# 2.3.5節  内包 --- enumerate や zip　　zipの例
towers = ['東京タワー', '通天閣', '名古屋テレビ塔']
heights = [330, 108, 180]
for u in zip(towers, heights):
    print(u)
