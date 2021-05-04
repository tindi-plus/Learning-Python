# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:25:35 2021.

Cleaning tweets

@author: Tindi.Sommers
"""
from textblob import TextBlob
import tweepy
import keys
from operator import itemgetter
from tweetlistener import TweetListener
import preprocessor as p
from textblob.utils import lowerstrip

#authenticate with Twitter and create an api
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = api.search(q='liverpool', count=100)

# initialize the preprocessor
p.set_options(p.OPT.URL, p.OPT.RESERVED, p.OPT.NUMBER, p.OPT.SMILEY, p.OPT.EMOJI,
              p.OPT.MENTION, p.OPT.HASHTAG)

clean = []
for tweet in search:
    try:
        text = tweet.extended_tweet.text
    except:
        text = tweet.text
    clean.append(p.clean(text))

stripped_text = [lowerstrip(t) for t in clean]

for text in stripped_text:
    print(text)
    print()
