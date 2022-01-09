# get SEB bank transactions into suitable format for google sheets

import sys
import re
import pygsheets
from datetime import date

headers = ["Bokföringsdatum", "Valutadatum", "Verifikationsnummer", "Text/mottagare ", "Belopp", "Saldo", "Invoice number", "VAT", "Notes"]		

with open('config.txt') as f:
    conf = dict([line.split() for line in f])

sheet = (conf["SHEET"])
gc = pygsheets.authorize()  
sh = gc.open_by_key(sheet)

# create a worksheet for the current month and switch to it
today = date.today()
newsheet = today.strftime("%B %Y")
sh.add_worksheet(newsheet,rows=1, cols=9) 
worksheet = sh.worksheet('title',newsheet)

# set the titles in the first row
worksheet.update_row(worksheet.rows, headers)

# what file are we looking for
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

		worksheet.add_rows(1) 
		worksheet.update_row(worksheet.rows, list(matches[0]))