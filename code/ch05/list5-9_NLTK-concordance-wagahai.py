# -*- coding: utf-8 -*-
# リスト 5-9 「吾輩」をキーワードにした KWIC 検索プログラム例
# NLTK Concordanceの情報は  http://www.nltk.org/api/nltk.html
from aozora import Aozora
import MeCab
import nltk

aozora = Aozora("wagahaiwa_nekodearu.txt")
m = MeCab.Tagger("-Owakati -b65535")   # MeCabのインスタンス生成（分かち書き）
string = m.parse( '\n'.join(aozora.read()) )  # 分かち書きに変換する
text = nltk.Text( nltk.word_tokenize(string) )
             # NLTKでトークン化しTextのフォーマットに変換する
word = '吾輩'                        # 検索語
c = nltk.text.ConcordanceIndex( text )
             # ConcordanceIndexクラスのインスタンス生成、入力textを指定
c.print_concordance(word, width=40)  # 検索語wordでKWIC形式を表示
print(c.offsets(word))               # 検索語wordの位置情報を得る
