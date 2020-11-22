import os
import json
import tweepy

API_KEY = os.environ["TWITTER_API_KEY"]
API_SECRET_KEY = os.environ["TWITTER_API_SECRET_KEY"]

ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

def connect_to_twitter():
	auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY);
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET);
	api = tweepy.API(auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)
	return api

def get_timeline():
	api = connect_to_twitter()
	timeline = api.home_timeline(tweet_mode="extended")
	return timeline
