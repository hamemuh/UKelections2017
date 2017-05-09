TRACK_TERMS = ["Jeremy Corbyn",  "Corbyn", "Labour"] #, "Labour","Lib Dem",\
               #"Liberal Democrat",  "Green Party", "Prime Minister", "UKIP", "SNP",\
               # "Nicola Sturgeon", "Theresa May", "Conservative", "tories",\
               # "Caroline Lucas", "Jonathan Bartley"]
CONNECTION_STRING = ""
CSV_NAME = "tweets.csv"
TABLE_NAME = "election"

try:
    from private import *
except Exception:
    pass