# -*- coding: utf-8 -*-
# リスト 5-13  Stanford Parser のテストプログラム
from nltk.parse.stanford import *
p = StanfordParser( \
    path_to_jar='stanford-parser-full-2017-06-09/stanford-parser.jar', \
    path_to_models_jar = 'edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz' )
out = p.raw_parse('This is a pen.')
for u in out:
    print(u)

out = p.raw_parse_sents( ['This is a pen.', 'I have a book.'] )
for u in out:
    for v in u:
        print(v)

dep_p = StanfordDependencyParser( \
    path_to_jar='stanford-parser-full-2017-06-09/stanford-parser.jar', \
    path_to_models_jar = 'edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz' )
out = [list(parse.triples()) for parse in dep_p.raw_parse( \
                   "The quick brown fox jumps over the lazy dog.")]
for u in out:
    print(u)
