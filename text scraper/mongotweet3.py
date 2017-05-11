import settingsmongo
import privatemongo
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

            for word in settingsmongo.TRACK_TERMS:        # loop to pick out the filtered word in the TWEET (text) ONLY
                if td.get('text') and word in td['text']:

                    # to insert polarity etc into mongo
                    text = td['text']  # set the tweet to variable 'text'
                    td['polarity'] = TextBlob(text).sentiment.polarity  # calculates polarity of tweet and adds column to mongo
                    td['subjectivity'] = TextBlob(text).sentiment.subjectivity  # " " subjectivity " "

                    td['filter'] = word   # add column of the word that the tweet has been filtered by

                    if word in settingsmongo.Labour:        # to create 'bin' term for each filter word
                        td['Bin'] = 'Labour'
                    elif word in settingsmongo.Conservative:
                        td['Bin'] = 'Conservative'
                    elif word in settingsmongo.LibDem:
                        td['Bin'] = 'LibDem'
                    elif word in settingsmongo.UKIP:
                        td['Bin'] = 'UKIP'
                    elif word in settingsmongo.Green:
                        td['Bin'] = 'Green'
                    elif word in settingsmongo.SNP:
                        td['Bin'] = 'SNP'
                    elif word in settingsmongo.cymru:
                        td['Bin'] = 'Cymru'
                    elif word in settingsmongo.neutral:
                        td['Bin'] = 'Neutral'
                    elif word in settingsmongo.other:
                        td['Bin'] = 'other'
                    else:
                        i




                    db.final_tweets2.insert(td)  # insert all columns into mongo
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


auth = tweepy.OAuthHandler(privatemongo.TWITTER_APP_KEY, privatemongo.TWITTER_APP_SECRET)
auth.set_access_token(privatemongo.TWITTER_KEY, privatemongo.TWITTER_SECRET)
api = tweepy.API(auth)

KL = KubrickListener()
stream = tweepy.Stream(auth=api.auth, listener=KL)
stream.filter(track=settingsmongo.TRACK_TERMS)
