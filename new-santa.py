
# simplified secret santa just using lists

import random

names = ['Bill','Ben','Charles','Diana','Erika', 'Finbar', 'Terry', 'Jools', 'Alfred', 'Lars', 'Helen']
random.shuffle(names)    
print (names)

# slice list in two parts and append
# last element in front of the sliced list
       
# [names[-1]] --> converts last element of array into list
# to append in front of sliced list
# names[0:-1] --> list of elements except last element

print ([names[-1]] + names[0:-1])

#slicing syntax
#Lst[ Initial : End : IndexJump ]
#print ("slicing")
#print(names[::-1])

# *** another simple way *** 
for i, name in enumerate(names):
	print (name + " gives to " + names[i-1]) 