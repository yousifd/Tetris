#A B C D
#E F G H

# make blocks
# make function that randomly chooses blocks

import time

MOVMENT_CONSTANT = 1
BOTTOM = -100

choice = None
block = {'A':1} #this is Block
y = 0 # this is the top of the screen 

while True:
    choice = raw_input('1 for playing, 0 for kill: ')
    if choice == '1':
        #start game
        while y > BOTTOM: 
            y -= MOVMENT_CONSTANT 
            print y
            time.sleep(1)
        break
        
    elif choice == '0':
        #end game
        print 0
        break
    else:
        print 'Invalid Input'    