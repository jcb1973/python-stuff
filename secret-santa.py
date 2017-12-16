from random import *
import copy
import inflect

ITERATION_MAX = 3

p = inflect.engine()

with open("names.txt") as f:
    names = f.readlines()
    names = [x.strip() for x in names]

santas = list(names)
recipients = list(names)

iteration_counter = 0
done = False

while not done:
    
    the_list = []
    iteration_counter = iteration_counter + 1
    
    if iteration_counter == ITERATION_MAX:
        break
    
    santas = list(names)
    recipients = list(names)
    
    done = False
    failed = False
    
    for santa in copy.copy(santas):
        failed = False
        santa_needs_present=False
        
        # only *give* present once
        santas.remove(santa)
        
        # make sure we don't give ourselves a present
        if santa in recipients:
            santa_needs_present=True
            recipients.remove(santa)
        
        if not recipients:
            # shuffled in such a way as to give self present, try again...
            done = False
            failed = True
        else:
            recipient = sample(recipients, 1)
            # put santa back in pool if they haven't had present yet
            if santa_needs_present:
                recipients.append(santa)
            
            the_list.append(santa + " gives present to " + recipient[0])
            
            # make sure noone *gets* more than one present
            recipients.remove(recipient[0])
    
    if not failed:
        done = True

if iteration_counter == ITERATION_MAX:
    print ("Could not set Santas in", ITERATION_MAX, p.plural("iteration",ITERATION_MAX))
else:
    for combo in the_list:
        print (combo)
