# -*- coding: utf-8 -*-
# 2.3.6節  ラムダ式
def extract_height(u):
    return u[1]
p = [['東京タワー', 330], ['通天閣', 108], ['名古屋テレビ塔', 180]]
q = sorted(p, key=extract_height)
print(q)

p = [['東京タワー', 330], ['通天閣', 108], ['名古屋テレビ塔', 180]]
q = sorted(p, key=lambda u: u[1])
print(q)

dic = {'東京タワー': 333, '富士山': 3776, '通天閣': 108, '天保山': 4.53}
print(sorted(dic.items(), key=lambda u: u[1]))

print(sorted(dic.items(), key=lambda u: u[1], reverse=True))
