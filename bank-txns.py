# get SEB bank transactions into suitable format for google sheets

import sys
import re
import pygsheets
import random
from pygsheets import custom_types
from datetime import date
import argparse

headers = ["Bokföringsdatum", "Valutadatum", "Verifikationsnummer", "Text/mottagare ", "Belopp", "Saldo", "Invoice number", "VAT", "Notes"]

parser = argparse.ArgumentParser("Puts values from CSV file in spreadsheet (specified in 'config.txt')")
parser.add_argument('--file', required=True)
parser.add_argument('--testing', default=True)
args = parser.parse_args()

# which sheet are we using
with open('config.txt') as f:
    conf = dict([line.split() for line in f])
sheet = (conf["SHEET"])
if (args.testing):
	sheet = (conf["TESTING-SHEET"])

# authorize
gc = pygsheets.authorize(client_secret='client_secret.json')
sh = gc.open_by_key(sheet)

# create a worksheet for the current month and switch to it
new_sheet_name = date.today().strftime("%B %Y")
if (args.testing):
	new_sheet_name = date.today().strftime("%B %Y") + str(random.randint(1, 9999))
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

with open(args.file, 'r', encoding='utf-8') as txnsFile:

	for row in txnsFile:
		matches = (solution.findall(row))
		for match in matches:
			#
			# convert string items 4 and 5 in list to signed floats in place
			#
			new_list = [float((v.replace("\xad", "-").replace(".","").replace(",",".")))
				if (i == 4) or (i == 5)
				# leave others as is
				else v for i,v in enumerate(match)]
			if not args.testing:
				worksheet.add_rows(1)
				worksheet.update_row(worksheet.rows, new_list)
			else:
				print ("would add ")
				print (new_list)

		if args.testing:
			print ("completed")
			exit

# formatting
model_cell = pygsheets.Cell('D1')
model_cell.horizontal_alignment=custom_types.HorizontalAlignment.LEFT
pygsheets.DataRange('C1', 'D%s' % worksheet.rows, worksheet=worksheet).apply_format(model_cell)

model_cell = pygsheets.Cell('A1')
model_cell.set_text_format("bold", True)
pygsheets.DataRange(start='A1', end='I1', worksheet=worksheet).apply_format(model_cell)
