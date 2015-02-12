#A B C D
#E F G H

# make blocks
# make function that randomly chooses blocks

block = {'A':1} #this is Block
y = 0 #this is top of screen
x = 0 #this is center of screen
#speed = 1

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
    #global speed
    if symbol == key.LEFT:
        x -= MOVMENT_CONSTANT
	print 'X:', x
    elif symbol == key.RIGHT:
	x += MOVMENT_CONSTANT
	print 'X:', x
    elif symbol == key.DOWN:
	#speed = 2
	#print 'Speed:', speed
	print 'faster'
    elif symbol == key.ESCAPE:
	window.close()
	pyglet.app.exit()

#----------------
#we difine a function that stores the current values of y and x
#---------------

def fall(dt):
    global y
    #global speed
    if y > BOTTOM:
	y -= MOVMENT_CONSTANT # * speed)
	print 'Y:', y
	speed = 1

pyglet.clock.schedule_interval(fall, 1)

pyglet.app.run()    

window.close()
pyglet.app.exit()
