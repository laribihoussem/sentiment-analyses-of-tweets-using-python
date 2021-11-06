# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = open('hello.txt', encoding='UTF-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','', string.punctuation))

tokenized_words = word_tokenize(cleaned_text,"english")



final_words=[]
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

emotion_list = []

with open('emotions.txt', 'r') as file :
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'",'').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg < pos :
        print("positive sentiment")
    elif pos < neg:
        print("negative sentiment")
    else:
        print("neutral sentiment")


    print(score)

sentiment_analyse(cleaned_text)
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()