#A B C D
#E F G H

choice = None
block = {'A':1} #this is Block 

while True:
    choice = raw_input('1 for playing, 0 for kill: ')
    if choice == '1':
        #start game
        print 1
        break
    elif choice == '0':
        #end game
        print 0
        break
    else:
        print 'Invalid Input'    