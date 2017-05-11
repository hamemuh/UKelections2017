import json
import pandas as pd
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
import pymongo

connection = pymongo.MongoClient('10.50.0.128', 27017) # connecting to mongo
db = connection.twitterdb

tweets = db.testfilter3.find({}, {"text": 1, "polarity": 1, "subjectivity": 1, "filter": 1,"Bin": 1, "created_at": 1}) # pulling tweets from mongo
#l = []
#for tweet in tweets:
    #l.append(tweet)

l = [t for t in tweets]

df = DataFrame(l)
print df








