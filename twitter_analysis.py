import csv

import tweepy
import string
import re

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)
csvFile = open('twitter_search.csv', 'a')
csvWriter = csv.writer(csvFile)

search_words = "#lonely"  # enter your words
new_search = search_words + " -filter:retweets"

for tweet in tweepy.Cursor(api.search, q=new_search, count=100,
                           lang="en",
                           since_id=0).items(10
s):
    print(tweet.text)
    csvWriter.writerow([tweet.text.encode('utf-8')])

