import pymongo
import pandas as pd
from pandas import DataFrame, Series
from pymongo import MongoClient
import json
import plotly
plotly.tools.set_credentials_file(username = 'mn1510', api_key = 'oAuitQzjIHqN4P87gPoA')
import cufflinks
import datetime
from bson.objectid import ObjectId
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

client = MongoClient(host = '10.50.0.128:27017')
db = client.twitterdb
collection = db.final_tweets3

pipe = [{"$match": {"_id": {"$lt": ObjectId("591cd5f00000000000000000")}}}, \
       {"$project":{"tweet": "$text", "Category": "$Bin", "Polarity": "$polarity", "Subjectivity": "$subjectivity",  \
       "Date" : "$created_at", "_id" : 0}} ]

p = collection.aggregate(pipeline=pipe)

testlist = list(p)

print 'list is done'

Vaderscores = [SentimentIntensityAnalyzer().polarity_scores(i['tweet']) for i in testlist]

dfnew = DataFrame(testlist)

dfnew['VaderSentiment'] = Vaderscores

a = dfnew.to_dict(orient = 'records')

coll = db.beforeseventeenth

for item in a:
    coll.insert_one(item)

print 'success!'
