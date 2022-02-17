import re

solution = re.compile(r"""
	(\d{4}-\d{2}-\d{2}\s) 		# (1) date YYYYMMDD, space
	(.*)	
	""", re.VERBOSE)

gratitude_dict = {}

date = re.compile('(\d{4}-\d{2}-\d{2})(.*)')

with open("Presently.csv", 'r', encoding='utf-8') as txnsFile:

	date_index = ""

	for row in txnsFile:
		#print ("new row " + row)
		m = date.search(row)
		if m:
			date_index = m.group(1)
			gratitude_dict[date_index] = []
			gratitude_dict[date_index].append(m.group(2))
		else:
			gratitude_dict[date_index].append(row)

#print (type(gratitude_dict))
#for key in a_dict:
#...     print(key, '->', a_dict[key])

for entry in gratitude_dict:
	print (entry + "," + str(len(gratitude_dict[entry])) + "," + str(len(str(gratitude_dict[entry])) ))
	#print (entry + " " + str(gratitude_dict[entry]))