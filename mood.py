import re

gratitude_dict = {}

date = re.compile('(\d{4}-\d{2}-\d{2})(.*)')

with open("Presently.csv", 'r', encoding='utf-8') as txnsFile:

	date_index = ""

	for row in txnsFile:
		m = date.search(row)
		if m:
			date_index = m.group(1)
			gratitude_dict[date_index] = []
			gratitude_dict[date_index].append(m.group(2))
		else:
			gratitude_dict[date_index].append(row)

for entry in gratitude_dict:
	print (entry + "," + str(len(gratitude_dict[entry])) + "," + str(len(str(gratitude_dict[entry])) ))