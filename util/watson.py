import os
import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

WATSON_KEY = os.environ['WATSON_API_KEY']
WATSON_URL = os.environ['WATSON_URL']

def connect_to_watson():
	authenticator = IAMAuthenticator(WATSON_KEY)
	visual_recognition = VisualRecognitionV3(
    	version='2018-03-19',
    	authenticator=authenticator
	)
	visual_recognition.set_service_url(WATSON_URL)
	return visual_recognition

def process_images(timeline):
	visual_recognition = connect_to_watson()
	for tweet in timeline:
		if tweet.entities.get('media'):
			url = tweet.entities.get('media')[0]['media_url_https']
			classes_result=visual_recognition.classify(url=url).get_result()
			obj=classes_result['images'][0]['classifiers'][0]['classes']
			desc = "Image may contain: "
			for each in obj:
				desc = desc + each['class'] + ", "
			tweet.entities.get('media')[0]['classification']=desc
	return timeline

def fake_process_images(timeline):
	for tweet in timeline:
		if tweet.entities.get('media'):
			desc = "Image may contain: \n"
			tweet.entities.get('media')[0]['classification']=desc
	return timeline

