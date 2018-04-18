import time
import datetime
from datetime import date 

nosugar = date(2018,4,18)
noalcohol = date(2018,4,18)

today = datetime.date.today()
total_days = abs(today - nosugar).days

print ("To: jcb1973@gmail.com")
print ("Subject:", total_days, "days without sugar")
print ("From: jcb1973@googlemail.com")
print ("")
print ("Now it's", abs(today - nosugar).days, "days without sugar and", 
    abs(today - noalcohol).days, "days without alcohol")
