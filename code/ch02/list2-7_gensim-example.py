# -*- coding: utf-8 -*-
# リスト 2-7  潜在的意味解析モデルを使って話題を抽出するプログラム例
#
from gensim import corpora, models, similarities
# textsをあらかじめ準備しておく（分かち書き文のリスト）
num_topics = 3
documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]
# remove words that appear only once
all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once]
         for text in texts]
dictionary = corpora.Dictionary(texts)  # 入力textsをdictionaryに変換
corpus = [dictionary.doc2bow(text) for text in texts]  # corpusを作成
tfidf = models.TfidfModel(corpus)       # TFIDFモデルを作成
corpus_tfidf = tfidf[corpus]            # corpusをTF-IDFで重要語のみに変換
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topics)
                                        # corpus_tfidfからLSIモデルを作成
# トピックの表示
print(lsi.show_topics(num_topics, formatted=True))     # topicを表示
corpus_lsi = lsi[corpus_tfidf]          # corpus_tfidfのすべての文をLSIに変換
for doc in corpus_lsi:
    x = [ sorted(doc, key=lambda u: u[1], reverse=True) for u in doc if len(u)!=0]
    print(x)
