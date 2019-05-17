# -*- coding: utf-8 -*-
# 2.5.4節  ツイッターのデータ　　ツイッターデータのアクセス方法
from nltk.twitter import Twitter
tw = Twitter()
tw.tweets(keywords='happy', limit=10)
