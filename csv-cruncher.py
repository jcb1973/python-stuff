import csv

with open("feedback-received.csv", "rb") as csvFile:
    reader = csv.reader(csvFile, delimiter=',', quotechar='"')
    current_person = ""
    last_person = ""
    counter = 0
    running_total = 0
    new = 0
    
    for row in reader:
        current_person = row[3]
        
        if current_person == last_person:
            new = 0
            counter = counter + 1
            running_total = running_total + int(row[4]) + int(row[6]) + int(row[8])
        else:
            if counter > 0:
                avg = float(running_total / float(counter * 3.0)) 
                #print "%s gave total %d for %d people which is %.2f average" % (last_person, running_total, counter, avg)
                print "%s, %.2f" % (last_person, avg)
            running_total = int(row[4]) + int(row[6]) + int(row[8])
            new = 1 
            counter = 1
        
        last_person = current_person
        
#print "%s gave total %d for %d people which is %.2f average" % (last_person, running_total, counter, avg)
print "%s, %.2f" % (last_person, avg)