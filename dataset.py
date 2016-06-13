import tweepy
import json

import auth


def get_tuits(n, hashtag):
  api = auth.auth()

  tuits = []
  for status in tweepy.Cursor(api.search, q=hashtag).items(n):
    tuit = {
      "text": json.dumps(status.text),
      "location": json.dumps(status.user.location),
      "geo": json.dumps(status.geo)
    }
    # print tuit
    # tuit = json.dumps(status.text)
    tuits.append(tuit)

  with open('DATASETS/tuits-{}-{}.json'.format(n, hashtag), 'w') as outfile:
    json.dump(tuits, outfile)


get_tuits(100, 'PrayForOrlando')
