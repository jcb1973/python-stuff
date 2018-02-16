import csv

with open('choice.csv') as choices:
    r = csv.reader(choices, delimiter=',')
    
    for record in r:
        if len(record) > 1:
            print(record[2])
            print("Hi", record[1], "! \n\nJust to remind you that you ordered\n", record[3], \
                "and", record[4], "\nfor lunch, and\n", record[5], "and", record[6],
                "\nfor dinner.\n\n Enjoy the workshop!")
            print("\n")
