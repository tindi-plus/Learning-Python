# -*- coding: utf-8 -*-
"""
Created on Mon May  3 09:25:16 2021.

Percentage of English Tweets

@author: Tindi.Sommers
"""
import tweepy
import keys

#authenticate with Twitter and create an api
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#search and grab tweets about liverpool
cursor = tweepy.Cursor(api.search, q='liverpool', count=100)

#get the language property of each tweet and keep counts of the languages

languages = {}

for tweet in cursor.items(2000):
    # if the language key is already saved in the dic, increment the count, but
    # if it is not saved, create the key and assign its value as 1.
    if tweet.lang in languages.keys():
        languages[tweet.lang] += 1
    else:
        languages[tweet.lang] = 1

# sum all the frequency of the languages
total = 0
for freq in languages.values():
    total += freq

for lang in languages.items():
    print(f'{lang[0]}: {lang[1]}, {lang[1] / total:.2%}')