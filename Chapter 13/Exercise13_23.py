# -*- coding: utf-8 -*-
"""
Created on Fri May  7 18:08:25 2021.

Predictiing movie revenues
2021-05-07 17:54:15

@author: Tindi.Sommers
"""
from textblob import TextBlob
import tweepy
import keys
import preprocessor as p
from textblob.utils import lowerstrip
from datetime import date, datetime, time, timedelta

#authenticate with Twitter and create an api
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# the search api can return a maximum of 100 results at a time
cursor = tweepy.Cursor(api.search, q='The Matrix 4 since:2021-05-2', count=100)

# create a list of the tweet time stamps
tweet_times = [tweet.created_at for tweet in cursor.items(2000)]

print(len(tweet_times))

# create datetimes from the date strings from tweets
# tweet_times_obj = [datetime.strptime(t, '%Y-%m-%d %H:%M:%S') for t in tweet_times]

# sort the times objects into ascending order
sorted_times = sorted(tweet_times)

# get the time difference between the first tweet and the latest tweet
time_diff = sorted_times[len(sorted_times) - 1] - sorted_times[0]

# convert the time diff in days to seconds and divide by the total number of tweets
tweet_rate = len(tweet_times) / (time_diff.days * 24)

print(tweet_rate, 'per hour')
print()


