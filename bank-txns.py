# get SEB bank transactions into suitable format for google sheets
#txn-date, book-date, reference, desc, amount, balance		
#2021­12­06 2021­12­04 5484753649 Postnord se /21­12­03 ­199,00 14.273,86 

import sys
import re
import pygsheets
from datetime import date

with open('config.txt') as f:
    conf = dict([line.split() for line in f])

sheet = (conf["SHEET"])
gc = pygsheets.authorize()  
sh = gc.open_by_key(sheet)

# create a worksheet for the current month
today = date.today()
newsheet = today.strftime("%B %Y")
print("newsheet =", newsheet)
sh.add_worksheet(newsheet,rows=250, cols=9) 

txns = str(sys.argv[1])

solution = re.compile(r"""
	(\d{4}.\d{2}.\d{2}\s)
	(\d{4}.\d{2}.\d{2}\s)
	(\d*\s)
	(.*\s)
	(.*)
	(\s.*)
	(\s.*$)
	""", re.VERBOSE)

with open(txns, 'r', encoding='utf-8') as txnsFile:
    
	for row in txnsFile:
		matches = (solution.findall(row))
    	
		for match in matches:
			print(" ; ".join(match))