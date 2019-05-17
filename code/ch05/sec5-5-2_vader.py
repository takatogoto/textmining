# -*- coding: utf-8 -*-
# 5.5.2��  NLTK �� sentiment analysis �p�b�P�[�W�̗�  VADER �p�b�P�[�W�ɂ�銴��l�̌v�Z
from nltk.sentiment.vader import SentimentIntensityAnalyzer
vader_analyzer = SentimentIntensityAnalyzer()
sent = 'I am happy'
result = vader_analyzer.polarity_scores(sent)
print(sent + '\n', result)
result = vader_analyzer.polarity_scores('I am sad')
print(result)
result = vader_analyzer.polarity_scores('I am happy :-)')
print(result)
