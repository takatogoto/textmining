# -*- coding: utf-8 -*-
# リスト 5-12  英文 WordNet を NLTK から利用するプログラム例
# NLTK パッケージのファイル wordnet.py に含まれているデモプログラムから抜粋
#
# 前準備
import nltk
from nltk.corpus import wordnet
from nltk.corpus.reader import WordNetCorpusReader, WordNetICCorpusReader
wn = WordNetCorpusReader(nltk.data.find('corpora/wordnet'), None)
S = wn.synset
L = wn.lemma

# synsetの基本メソッド
s = S('go.v.21')        # 単語goの動詞の21番のsynsetを読み出す
# synsetの名前がmove.v.15 pos（品詞名）がv 辞書ファイルがverb.competition
print(s.name(), s.pos(), s.lexname())
print(s.lemma_names())  # synset goの語彙は['move', 'go']
print(s.definition())   # goの定義は"have a turn; make one's move in a game"
print(s.examples())     # goの例文は['Can I go now?']

# リンクをたどってみる
s = S('dog.n.01')
print(s.hypernyms())
    # dogの上位概念は[Synset('canine.n.02'), Synset('domestic_animal.n.01')]
print(L('zap.v.03.nuke').derivationally_related_forms())
    # [Lemma('atomic_warhead.n.01.nuke')]
print(L('zap.v.03.atomize').derivationally_related_forms())
    # [Lemma('atomization.n.02.atomization')]
 
print(s.member_holonyms())  # [Synset('canis.n.01'), Synset('pack.n.06')]
print(s.part_meronyms())    # [Synset('flag.n.07')]
print(S('Austen.n.1').instance_hypernyms())
    # Austenが例であるような上位概念[Synset('writer.n.01')]
print(S('composer.n.1').instance_hyponyms())
    # 作家の例（作曲家が多数表示される）

print(S('faculty.n.2').member_meronyms())
    # 一部分（メンバー）[Synset('professor.n.01')]
print(S('copilot.n.1').member_holonyms())
    # これが含まれる大きな集合[Synset('crew.n.01')]
print(S('table.n.2').part_meronyms())
    # 一部分[Synset('leg.n.03'), Synset('tabletop.n.01'), Synset('tableware.n.01')]
print(S('course.n.7').part_holonyms())  # 含まれる集合[Synset('meal.n.01')]
print(S('water.n.1').substance_meronyms())
    # 一部分（材料）[Synset('hydrogen.n.01'), Synset('oxygen.n.01')]
print(S('gin.n.1').substance_holonyms())  # 含まれる集合（材料）
    # [Synset('gin_and_it.n.01'), Synset('gin_and_tonic.n.01'),
    #  Synset('martini.n.01'), Synset('pink_lady.n.01')]
print(S('snore.v.1').entailments())  # 論理的な結論[Synset('sleep.v.01')]
print(S('heavy.a.1').similar_tos()) 
    #  [Synset('dense.s.03'), Synset('doughy.s.01'), Synset('heavier-than-air.s.01'),
    #   Synset('hefty.s.02'), Synset('massive.s.04'), Synset('non-buoyant.s.01'),
    #   Synset('ponderous.s.02')]
print(S('light.a.1').attributes())            # 属性[Synset('weight.n.01')]
print(S('heavy.a.1').attributes())            # 属性[Synset('weight.n.01')]

print(S('person.n.01').root_hypernyms())
    # 意味トリーのルート[Synset('entity.n.01')]

# 二者の関係（二者の間で初めて共通する概念）
print(S('person.n.01').lowest_common_hypernyms(S('dog.n.01')))  # 初めて共通する概念
    # 結果は[Synset('organism.n.01')]
print(S('woman.n.01').lowest_common_hypernyms(S('girlfriend.n.02')))
    # 結果は[Synset('woman.n.01')]

# 類似性指標。以下の指標の説明は、NLTKのドキュメント
# http://www.nltk.org/howto/wordnet.htmlにある
print(S('dog.n.01').path_similarity(S('cat.n.01')))   # パスで見たノードの近さ0.2
print(S('dog.n.01').path_similarity(S('wolf.n.01')))  # パスで見たノードの近さ0.333
print(S('dog.n.01').lch_similarity(S('cat.n.01')))
    # Leacock-Chosorowの類似度2.028
print(S('dog.n.01').wup_similarity(S('cat.n.01')))  # Wu-Palmer Similarity 0.857
wnic = WordNetICCorpusReader(nltk.data.find('corpora/wordnet_ic'), '.*\.dat')
ic = wnic.ic('ic-brown.dat')
print(S('dog.n.01').jcn_similarity(S('cat.n.01'), ic))
    # Information ContentによるJiang-Conrathの類似度0.4498
ic = wnic.ic('ic-semcor.dat')
print(S('dog.n.01').lin_similarity(S('cat.n.01'), ic))
    # Information ContentによるLinの類似度0.8863

print(S('code.n.03').topic_domains())
    # topic domain [Synset('computer_science.n.01')]
print(S('pukka.a.01').region_domains())  # region domain [Synset('india.n.01')]
print(S('freaky.a.01').usage_domains())  # usage domain [Synset('slang.n.02')]
