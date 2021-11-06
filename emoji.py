from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

b = b'\xF0\x9F\x91\xAE ACAB'
txt = b.decode('utf-8')
print(txt)


score = SentimentIntensityAnalyzer().polarity_scores('angry')
print(score)