# -*- coding: utf-8 -*-
# 2.3.5節  内包 --- enumerate や zip  リスト内包の例
input = [1, 3, 5, 7, 9]
output = []  #                   ←空のリストを作る
for u in input:
    output.append(u*2)  #        ←u*2の要素を1つずつ追加
print(output)           #        ←結果は[2, 6, 10, 14, 18]

output = [u*2 for u in input]
print(output)           #        ←結果は[2, 6, 10, 14, 18]

output = [u*2 for u in input if u>=3]
print(output)           #        ←結果は[2, 6, 10, 14, 18]

input = {'東京タワー': 333, '富士山': 3776, '通天閣': 108, '天保山': 4.53}

output = { u:v/1000 for u,v in input.items() }
print(output)           # 結果は\{'東京タワー': 0.333, '富士山': 3.776, '通天閣': 0.108, '天保山': 0.00453\}
