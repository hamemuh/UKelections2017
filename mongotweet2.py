import settingsmongo
import PrivateMongo
import tweepy
import dataset
from textblob import TextBlob

import json
import sys
import pymongo
MONGO_HOST = 'mongodb://localhost//twitterdb'#



class KubrickListener(tweepy.StreamListener):
    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False
    def on_data(self, status):





        try:

            connection = pymongo.MongoClient()
            db = connection.twitterdb           # to connect to mongo


            td = json.loads(status)  # load tweet in json dictionary format
            text = td['text']    # set the tweet to variable 'text'
            # to insert polarity etc into mongo
            td['polarity'] = TextBlob(text).sentiment.polarity   # calculates polarity of tweet and adds column to mongo
            td['subjectivity'] = TextBlob(text).sentiment.subjectivity  # "" subjectivity ""

            tweets = api.search(q="place:%s" % place_id)
            for tweet in tweets:
                print tweet.text + " \n\n " + tweet.place.name if tweet.place else "Undefined place"

            db.test123.insert(td)  # Insert into mongo ...Need to change name of this collection...

            print '___: D___'
        except:

            print 'error. sorry'

    def on_error(self, status_code):
        if status_code == 420:
            #  returning False in on_data disconnects the stream
            return False


auth = tweepy.OAuthHandler(privatemongo.TWITTER_APP_KEY, privatemongo.TWITTER_APP_SECRET)
auth.set_access_token(privatemongo.TWITTER_KEY, privatemongo.TWITTER_SECRET)
api = tweepy.API(auth)

places = api.geo_search(query="name of country", granularity="country")
place_id = places[0].id

KL = KubrickListener()
stream = tweepy.Stream(auth=api.auth, listener=KL)
stream.filter(track=settingsmongo.TRACK_TERMS)