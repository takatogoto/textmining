# -*- coding: utf-8 -*-
# 5.5.3節  日本語文の感情値分析  『吾輩は猫である』の解析
import re
import MeCab
from aozora import Aozora

pndicfname = "../pn_ja.dic"    #  高村氏の感情値辞書ファイルを指定
aozora = Aozora("../../../aozora/wagahaiwa_nekodearu.txt")
#aozora = Aozora("../../../aozora/hashire_merosu.txt")

def readpndic(filename):
    with open(filename, "r") as dicfile:
        items = dicfile.read().splitlines()
    return {u.split(':')[0]: float(u.split(':')[3]) for u in items}

pndic = readpndic(pndicfname)

# 文に分解する
string = '\n'.join(aozora.read())
string = re.sub('　', '', string)
string = re.split('。(?!」)|\n', re.sub('　', '', string))
while '' in string:  string.remove('')  # 空行を除く

m = MeCab.Tagger("-Ochasen")  # mecabで品詞分解する

# 文単位で形態素解析し、名詞だけ抽出し、基本形を文ごとのリストにする
sentensewordlist = [ \
    [v.split()[2] for v in m.parse(sentense).splitlines() \
       if (len(v.split())>=3 and v.split()[3][:2] in ['名詞','形容','動詞','副詞'])]  \
    for sentense in string]
for sentense in sentensewordlist[3:9]:
    pnlist = [pndic.get(v) for v in sentense if pndic.get(v)!=None]
    print('対象語', [v for v in sentense if pndic.get(v)!=None], '語の感情値', pnlist, '感情値の合計', sum(pnlist), '語数', len(pnlist), '平均', sum(pnlist)/len(pnlist) )
