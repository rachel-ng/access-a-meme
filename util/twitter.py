import os
import json
import tweepy

DIR = os.path.dirname(__file__) or '.'
DIR += '/'

with open(DIR+'twitter.json', 'r') as f:
	data = json.load(f)

API_KEY = data["API_KEY"]
API_SECRET_KEY = data["API_SECRET_KEY"]

ACCESS_TOKEN = data["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = data["ACCESS_TOKEN_SECRET"]

def connect_to_twitter():
	auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY);
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET);
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	return api

def get_timeline():
	api = connect_to_twitter()
	timeline = api.home_timeline()
	return timeline
