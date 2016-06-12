import tweepy
import json

import auth


def get_tuits(n, hashtag):
  api = auth.auth()

  tuits = []
  for status in tweepy.Cursor(api.search, q=hashtag).items(n):
    tuit = json.dumps(status.text)
    tuits.append(tuit)

  with open('DATASETS/tuits-{}-{}.json'.format(n, hashtag), 'w') as outfile:
    json.dump(tuits, outfile)


get_tuits(1000, '#bloodofmyblood')
