import Settings
import private
import tweepy
import dataset
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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

            for word in Settings.TRACK_TERMS:        # loop to pick out the filtered word in the TWEET (text) ONLY
                if td.get('text') and word in td['text']:

                    # to insert polarity etc into mongo
                    text = td['text']  # set the tweet to variable 'text'
                    td['polarity'] = TextBlob(text).sentiment.polarity  # calculates polarity of tweet and adds column to mongo
                    td['subjectivity'] = TextBlob(text).sentiment.subjectivity  # " " subjectivity " "
                    td['compound'] = SentimentIntensityAnalyzer().polarity_scores(text)

                    td['filter'] = word   # add column of the word that the tweet has been filtered by

                    if word in Settings.Conservative:
                        td['Bin'] = 'Conservative'
                    elif word in Settings.LibDem:
                        td['Bin'] = 'LibDem'
                    elif word in Settings.Labour:        # to create 'bin' term for each filter word
                        td['Bin'] = 'Labour'
                    elif word in Settings.UKIP:
                        td['Bin'] = 'UKIP'
                    elif word in Settings.Green:
                        td['Bin'] = 'Green'
                    elif word in Settings.SNP:
                        td['Bin'] = 'SNP'
                    elif word in Settings.Cymru:
                        td['Bin'] = 'Cymru'
                    elif word in Settings.neutral:
                        td['Bin'] = 'Neutral'
                    elif word in Settings.other:
                        td['Bin'] = 'other'
                    else:
                        i=1

                    td['stream_origin'] = 'text stream'
                    db.seventeenth_may.insert(td)  # insert all columns into mongo
                    db.CurrentTweets.insert(td)
                    print '___: D___'
                    print('Tweet found filtered by ' + word)

            else:
                print ' : ( ... no filter word in text'

        except:
            print 'error. sorry'

    def on_error(self, status_code):
        if status_code == 420:
            #  returning False in on_data disconnects the stream
            return False


auth = tweepy.OAuthHandler(private.TWITTER_APP_KEY, private.TWITTER_APP_SECRET)
auth.set_access_token(private.TWITTER_KEY, private.TWITTER_SECRET)
api = tweepy.API(auth)


KL = KubrickListener()
stream = tweepy.Stream(auth=api.auth, listener=KL)
stream.filter(track=Settings.TRACK_TERMS)
