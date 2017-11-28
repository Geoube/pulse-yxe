#!/usr/bin/env python
import tweepy
import time
import sys
import csv

# from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

# Some authentication stuff. Magic. Don't touch.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
# Let's define an error handler.
def getExceptionMessage(msg):
	words = msg.split(' ')

	errorMsg = ""
	for index, word in enumerate(words):
		if index not in [0,1,2]:
			errorMsg = errorMsg + ' ' + word
	errorMsg = errorMsg.rstrip("\'}]")
	errorMsg = errorMsg.lstrip(" \'")

	return errorMsg

# Little thing to make sure the auth credentials work.
def doSanityCheck():
	try:
	    user = api.me()
	except tweepy.TweepError as e:
	    print (e.api_code)
	    print (getExceptionMessage(e.reason))

	print('Mining under the name ' + user.name
		+ ' from ' + user.location
		+ ' following ' + str(user.friends_count) 
		+ ' people.')

# TODO: In the future, scrape tweets with the #yxe or #saskatoon hashtag as well.


doSanityCheck()

# Quick run of tweet time and location
for tweet in tweepy.Cursor(
	api.search,
	q = "#yxe",
	count = 100,
	).items(100):
    
    	print(tweet.created_at, tweet.author.location)
    	print('\n')
