#A B C D
#E F G H

# make blocks
# make function that randomly chooses blocks

choice = None
block = {'A':1} #this is Block
y = 0 #this is top of screen
x = 0 #this is center of screen

import time
import pyglet
from pyglet.window import key 

MOVMENT_CONSTANT = 1
BOTTOM = -30

#create a window
window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()

@window.event
def on_key_press(symbol, modifiers):
    global x #FIX(see bellow)
    if symbol == key.LEFT:
        x -= MOVMENT_CONSTANT
	print 'X:', x
    elif symbol == key.RIGHT:
	x += MOVMENT_CONSTANT
	print 'X:', x
    elif symbol == key.ESCAPE:
	window.close 

#----------------
#we difine a function that stores the current values of y and x
#---------------

def fall(dt):
    global y
    if y > BOTTOM:
	y -= MOVMENT_CONSTANT
	print 'Y:', y

pyglet.clock.schedule_interval(fall, 1)

while True:
    choice = raw_input('1 for playing, 0 for kill: ')
    if choice == '1':
        #start game
	x=0
	pyglet.app.run()
        break
    elif choice == '0':
        #end game
        print 0
        break
    else:
        print 'Invalid Input'    

window.close()
