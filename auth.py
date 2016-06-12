import json
import tweepy
from tweepy import OAuthHandler

def auth():
  with open('credentials.json') as credentials:
    data = json.load(credentials)

  consumer_key = data["consumer_key"]
  consumer_secret = data["secret"]
  access_token = data["access_token"]
  access_secret = data["access_secret"]

  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)

  api = tweepy.API(auth)

  return api
