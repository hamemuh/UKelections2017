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

            for hashtag in td['entities']['hashtags']:
                text2 = hashtag['text']                     # picks out the hashtag from the tweet
                print text2

                if text2.lower() in settingshash.TRACK_TERMS:  # picks out the filtered word in the TWEET (hashtag) ONLY
                   # to insert polarity etc into mongo
                    text = td['text']  # set the tweet to variable 'text'
                    td['polarity'] = TextBlob(text).sentiment.polarity  # calculates polarity of tweet and adds column to mongo
                    td['subjectivity'] = TextBlob(text).sentiment.subjectivity  # " " subjectivity " "

                    td['filter'] = text2
                     ## add column of the word that the tweet has been filtered by
                    print '___: D___'
                    print('Tweet found filtered by ' + text2)
    #
                    if text2.lower() in settingshash.Labour:        # to create 'bin' term for each filter word
                        td['Bin'] = 'Labour'
                    elif text2.lower() in settingshash.Conservative:
                        td['Bin'] = 'Conservative'
                    elif text2.lower() in settingshash.LibDem:
                        td['Bin'] = 'LibDem'
                    elif text2.lower() in settingshash.UKIP:
                        td['Bin'] = 'UKIP'
                    elif text2.lower() in settingshash.Green:
                        td['Bin'] = 'Green'
                    elif text2.lower() in settingshash.SNP:
                        td['Bin'] = 'SNP'
                    elif text2.lower() in settingshash.Cymru:
                        td['Bin'] = 'Cymru'
                    elif text2.lower() in settingshash.Neutral:
                        td['Bin'] = 'Neutral'
                    elif text2.lower() in settingshash.other:
                        td['Bin'] = 'Other'
                    else:
                        i=1

                    td['stream_origin'] = 'hashtag stream'  # column to say tweet has been picked out by its hashtag
                    db.final_tweets3.insert(td)




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
