# -*- coding: utf-8 -*-
# 5-7節  構文解析と係り受け解析の実際  Python から呼び出す例
import CaboCha
parser = CaboCha.Parser('-f3')
sentense = '今日は良い天気です。'
tree = parser.parse(sentense)  # 解析結果がtreeに入っている
tokens = {}
for i in range(tree.token_size()):
    token = tree.token(i)
    print('token.features', token.feature.split(','))

print('---')
chunk_surfaces = {}
for i in range(tree.chunk_size()):
    chunk = tree.chunk(i)
    for j in range(chunk.token_size):
        g = tree.token(chunk.token_pos + j)
        print('surface', g.surface)
        print('  features', g.feature.split(','))
    print('link', chunk.link)
    print('---')
