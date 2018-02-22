import time
import datetime
from datetime import date 

nosugar = date(2018,1,16)
nocoffee = date(2018,2,21)

today = datetime.date.today()

print ("Now it's", abs(today - nosugar).days, "days without sugar and", 
    abs(today - nocoffee).days, "days without coffee")
