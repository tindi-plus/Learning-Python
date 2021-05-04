# -*- coding: utf-8 -*-
"""
Created on Tue May  4 15:31:22 2021.

Live translation of the tweets

@author: Tindi.Sommers
"""

from textblob import TextBlob
import tweepy
import keys
from operator import itemgetter
from tweetlistener import TweetListener

#authenticate with Twitter and create an api
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

trends = api.trends_place(id=766273)

trends_list = trends[0]['trends']

# get all the trends with tweet_volume: ie tweets with tweet_volume above 10,000
trend_list = [t for t in trends_list if t['tweet_volume']]

trend_list = sorted(trend_list, key=itemgetter('tweet_volume'), reverse=True)

print(trend_list[0])
print()

tweet_listener =TweetListener(api)

stream = tweepy.Stream(api.auth, listener=tweet_listener)
stream.filter(track=[trend_list[0]['name']], is_async=True)


