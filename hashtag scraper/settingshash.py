TRACK_TERMS = [ "votelabour", "jc4pm", "jezwecan","forthemany", "voteconservative", "votelibdem", "voteukip", "votegreen",\
                "votesnp", "plaid17", "ge2017", "generalelection2017", "vote2017",  "election2017", "ukelection",\
                 "generalelection", "ge17", "june8th", "makevotesmatter","campaignlive", "forthemany",\
                "toriesout", "tories", "votegreen2017"]

Labour = ["votelabour", "jc4pm", "jezwecan", "forthemany"]
Conservative = [ "voteconservative"]
LibDem = ["votelibdem"]
UKIP = ["voteukip"]
Green = ["votegreen", "votegreen2017"]
SNP = ["votesnp"]
Cymru = ["plaid17"]
Neutral = ["ge2017", "generalelection2017", "vote2017",  "election2017", "ukelection", \
            "generalelection", "ge17", "june8th", "makevotesmatter","campaignlive"]
Other = [ "toriesout"]

CONNECTION_STRING = ""
CSV_NAME = "tweets.csv"
TABLE_NAME = "election"

try:
    from private import *
except Exception:
    pass