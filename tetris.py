#A B C D
#E F G H

# make blocks
# make function that randomly chooses blocks

import pyglet
from pyglet.window import key
from pyglet import clock

MOVMENT_CONSTANT = 1
BOTTOM = -100

block = {'A':1} #this is Block
y = 0 #this is top of screen
x = 0 #this is center of screen
 
def fall(dt):
    global y
    
    if y > BOTTOM:
	y -= MOVMENT_CONSTANT
	print 'Y:', y

#create a window
window = pyglet.window.Window()
clock.schedule_interval(fall, 1)

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
    elif symbol == key.DOWN:
        fall(0)
    elif symbol == key.UP:
        print 'Rotate'
    elif symbol == key.ESCAPE:
	window.close()
	pyglet.app.exit()
    
#----------------
#we difine a function that stores the current values of y and x
#---------------

pyglet.app.run()    

window.close()
pyglet.app.exit()
