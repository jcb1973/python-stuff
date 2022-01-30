# get SEB bank transactions into suitable format for google sheets

import sys
import re
import pygsheets
import random
from pygsheets import custom_types
from datetime import date

headers = ["Bokföringsdatum", "Valutadatum", "Verifikationsnummer", "Text/mottagare ", "Belopp", "Saldo", "Invoice number", "VAT", "Notes"]		

# what file are we looking for, are we in testing mode
txns = str(sys.argv[1])
testing_mode = str(sys.argv[2])

with open('config.txt') as f:
    conf = dict([line.split() for line in f])

if (testing_mode == "TEST"):
	print ("testing mode only")
	sheet = (conf["TESTING-SHEET"])
else:
	print ("live mode")
	sheet = (conf["SHEET"])

gc = pygsheets.authorize(client_secret='client_secret.json',)  
sh = gc.open_by_key(sheet)

# create a worksheet for the current month and switch to it
if (testing_mode == "TEST"):
	new_sheet_name = date.today().strftime("%B %Y") + str(random.randint(1, 9999))
else:
	new_sheet_name = date.today().strftime("%B %Y")
	
sh.add_worksheet(new_sheet_name,rows=1, cols=9) 
worksheet = sh.worksheet('title',new_sheet_name)

# set the titles in the first row
worksheet.update_row(worksheet.rows, headers)

solution = re.compile(r"""
	(\d{4}.\d{2}.\d{2}\s) 		# (1) date YYYYMMDD, space
	(\d{4}.\d{2}.\d{2}\s)	 	# (2) date YYYYMMDD, sapce
	(\S*?\s{1}) 				# (3) non greedy verification string, space
	(.*\s) 						# (4) greedy text string followed by space
	(.*,\d{2})\s 				# (5) amount string "n*,nn" before balance, space
	(.*,\d{2}) 					# (6) balance "n*,nn"
	""", re.VERBOSE)

with open(txns, 'r', encoding='utf-8') as txnsFile:
	
	for row in txnsFile:
		matches = (solution.findall(row))
		for match in matches:
			print (match)
			worksheet.add_rows(1) 
			worksheet.update_row(worksheet.rows, list(matches[0]))

# formatting
model_cell = pygsheets.Cell('D1')
model_cell.horizontal_alignment=custom_types.HorizontalAlignment.LEFT
pygsheets.DataRange('C1', 'D%s' % worksheet.rows, worksheet=worksheet).apply_format(model_cell)

model_cell = pygsheets.Cell('A1')
model_cell.set_text_format("bold", True)
pygsheets.DataRange(start='A1', end='I1', worksheet=worksheet).apply_format(model_cell)
