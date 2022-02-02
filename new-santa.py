
# simplified secret santa just using lists

import random

names = ['Bill','Ben','Charles','Diana','Erika', 'Finbar', 'Terry', 'Jools', 'Alfred', 'Lars', 'Helen']

random.shuffle(names)    
#print (names)
#Lst[ Initial : End : IndexJump ]
#print ("slicing")
#print(names[::-1])

for i, name in enumerate(names):
	print (name + " gives to " + names[i-1]) 