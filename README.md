# UKelections2017
Sentiment analysis to forecast the outcome of the UK 2017 snap election.


# Scraper files
There are currently two scraper files for ingesting tweets, one to pick out track terms in the text of the tweet, the other to pick out track terms in the hashtag of the tweet. 

The text scraper can be found in the 'text scraper' folder with the associated settings python script (settingsmongo.py - contains track terms) and 'private' python script (contains twitter API keys - needs to be renamed as "privatemongo" to work with the mongotweet3.py file)
The current, working twitter streamer is the file: mongotweet3.py

The hashtag scraper can be found in the 'hashtag scraper' folder with the associated settings python script (settingshash.py). In order to work, a copy of the private python script, found in the text scraper folder should be copied and renamed "privatehash.py" and stored in the same directory as the scraper and settings scripts. The current, working hashtag scraper file is named: "mongotweethash.py"


