TRACK_TERMS = ["Jeremy Corbyn",  "Corbyn", "Labour", "#votelabour", "conservative", "Theresa May", "David Cameron",\
               "#voteconservative", "Lib Dem", "Tim Farron", "Nick Clegg", "Vince Cable", "#votelibdem", "UKIP",\
               "Paul Nuttall", "Nigel Farage", "Peter Whittle", "#voteukip", "Green Party", "Caroline Lucas",\
               "Jonathan Bartley", "Amelia Womack", "#votegreen", "SNP", "Nicola Sturgeon", "Angus Robertson",\
               "Alex Salmond", "#votesnp", "generalelection2017", "Plaid Cymru","Leanne Wood",\
               "Dafydd Trystan Davies", "Gareth Clubb", "#voteplaidcymru","ge2017", "#generalelection2017",\
               "#vote2017", "#ge2017", "#election2017", "#ukelection", "uk election","General Election",\
               "#generalelection", "#ge17", "#june8th", "#MakeVotesMatter","#CampaignLive", "#forthemany",\
               "#toriesout", "#jc4pm", "#jezwecan", "#tories", "#votegreen2017" ]

Labour = ["Jeremy Corbyn",  "Corbyn", "Labour", "#votelabour"]
Conservative = ["conservative", "Theresa May", "David Cameron", "#voteconservative"]
LibDem = ["Lib Dem", "Tim Farron", "Nick Clegg", "Vince Cable", "#votelibdem"]
UKIP = ["UKIP", "Paul Nuttall", "Nigel Farage", "Peter Whittle", "#voteukip"]
Green = ["Green Party", "Caroline Lucas", "Jonathan Bartley", "Amelia Womack", "#votegreen"]
SNP = ["SNP", "Nicola Sturgeon", "Angus Robertson", "Alex Salmond", "#votesnp"]
Cymru = ["Plaid Cymru","Leanne Wood", "Dafydd Trystan Davies", "Gareth Clubb", "#voteplaidcymru"]
neutral = ["#ge2017", "#generalelection2017", "#vote2017", "#ge2017", "#election2017", "#ukelection", "uk election",\
           "#General Election", "#generalelection", "#ge17", "#june8th", "#MakeVotesMatter","#CampaignLive"]
other = ["#forthemany", "#toriesout", "#jc4pm", "#jezwecan", "#tories", "#votegreen2017"]

CONNECTION_STRING = ""
CSV_NAME = "tweets.csv"
TABLE_NAME = "election"

try:
    from private import *
except Exception:
    pass