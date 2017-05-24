import time
import urllib2
from bs4 import BeautifulSoup
import threading
import datetime as dt
import pymongo
import csv

# Program scrapes website every 3 hours for headlines
# first column : timestamp of scraping
# second column: bin name: 'headlines'
# third column: website name
# Other columns: Headlines

# stores in a text file in c:\Election

def headline():
    try:

        threading.Timer(10800, headline).start()  # timer - runs program every 3 hours


        news = "https://www.bbc.co.uk/news/election/2017"
        page = urllib2.urlopen(news)
        soup = BeautifulSoup(page, "lxml")      # load in webpage to beautiful soup
        title = soup.h3.string
        allhead = soup.findAll("h3")        # create variable with all 'h3' tags in
        timestamp = dt.datetime.today()     # create time stamp of when program was run
        binname = 'headlines'       # binname, may be useful to store in the text file
        data = []       # create list that all info will be added to


        #print binname
        data.append(str(timestamp))     # add 3 initial fields to list
        data.append('headlines')
        data.append(news)

        for h in allhead[0:27]:

            entry = str(h).split('>')[1][:-4]       # cleans h3 tag to just the text
            #print entry  # maybe just top 6
            data.append(entry)                      # add text of headline to data list


        print data
        print '\r'
                                                    # write data list to text file

        with open(r"C:\Election\twitter-scrape-master\newsheadlines.txt", 'a') as f:

            f.write('|'.join(data))

        with open(r"C:\Election\twitter-scrape-master\newsheadlines.txt", 'a') as f:
            f.write('\n')




    except:
        print 'error, sorry'



headline()