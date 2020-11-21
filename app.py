import os, random, json, urllib, sys, io
from flask import Flask, render_template, request, session, url_for, redirect, flash, make_response, send_file
from util import twitter, watson, process

sys.path.append('..')
sys.path.append('../util')


app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def root():
	timeline = twitter.get_timeline()
	timeline = watson.fake_process_images(timeline)
	timeline = process.process_tweets(timeline)
	#for tweet in timeline:
		#print(tweet)
	return render_template("base.html", timeline = timeline)

@app.route('/garbled')
def root():
	timeline = twitter.get_timeline()
	return render_template("base.html", timeline = timeline)


if __name__ == '__main__':
    app.debug = True
    app.run()





