# -*- coding: utf-8 -*-
# 5.5.2節  NLTK の sentiment analysis パッケージの例  VADER パッケージによる感情値の計算
from nltk.sentiment.vader import SentimentIntensityAnalyzer
vader_analyzer = SentimentIntensityAnalyzer()
sent = 'I am happy'
result = vader_analyzer.polarity_scores(sent)
print(sent + '\n', result)
result = vader_analyzer.polarity_scores('I am sad')
print(result)
result = vader_analyzer.polarity_scores('I am happy :-)')
print(result)
