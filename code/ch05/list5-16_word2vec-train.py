# -*- coding: utf-8 -*-
#  リスト 5-16 Word2Vec の学習フェーズのプログラム例
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', \
                    level=logging.INFO)

# jpwall.txtがコーパスファイル名
sentences = gensim.models.word2vec.Text8Corpus("wp2txt/jpwall.txt")

# jpwall.txtを学習させる
model = gensim.models.word2vec.Word2Vec(sentences, min_count=5)
print("model gen complete")
model.save("jpwmodel")  # モデルをファイルに保存
