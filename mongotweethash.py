import settingshash
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


            #text2 = td['entities']['hashtags']
            for hashtag in td['entities']['hashtags']:
                text2 = hashtag['text']
                print text2
                #for text2 in settingshash.TRACK_TERMS:        # loop to pick out the filtered word in the TWEET (text) ONLY
                if text2.lower() in settingshash.TRACK_TERMS:
                   # to insert polarity etc into mongo
                    text = td['text']  # set the tweet to variable 'text'
                    td['polarity'] = TextBlob(text).sentiment.polarity  # calculates polarity of tweet and adds column to mongo
                    td['subjectivity'] = TextBlob(text).sentiment.subjectivity  # " " subjectivity " "

                    td['filter'] = text2
                    db.anothertest.insert(td) ## add column of the word that the tweet has been filtered by
                    print '___: D___'
                    print('Tweet found filtered by ' + text2)
    #
                #if word in settingshash.Labour:        # to create 'bin' term for each filter word
                #    td['Bin'] =    'Labour'
                #elif word in settingshash.Conservative:
                #    td['Bin'] = 'Conservative'
                #elif word in settingshash.LibDem:
                #    td['Bin'] = 'LibDem'
                #elif word in settingshash.UKIP:
                #    td['Bin'] = 'UKIP'
                #elif word in settingshash.Gree n:
                #    td['Bin'] = 'Green'
                #elif word in settingshash.SNP:
                #    td['Bin'] = 'SNP'
                #elif word in settingshash.cymru:
                #    td['Bin'] = 'Cymru'
                #elif word in settingshash.neutral:
                #    td['Bin'] = 'Neutral'
                #elif word in settingshash.other:
                #    td['Bin'] = 'other'
                #else:
                #    i=1
    ##
                #db.anothertest.insert(td)  # insert all columns into mongo


            #else:
                #print ' : ( ... no filter word in text'
                #db.anothertestreject.insert(td)

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
stream.filter(track=settingshash.TRACK_TERMS)
