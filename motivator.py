import time
import datetime
from datetime import date 

with open('config.txt') as f:
    conf = dict([line.split() for line in f])

FROM = (conf["GMAIL_USER"])
TO = (conf["GMAIL_USER"])

nosugar = date(2018,1,16)
nocoffee = date(2018,2,21)

today = datetime.date.today()

print ("To: ", TO)
print("Subject: Keep on going...")
print("From: ", FROM)
print()
print ("Now it's", abs(today - nosugar).days, "days without sugar and", 
    abs(today - nocoffee).days, "days without coffee")
