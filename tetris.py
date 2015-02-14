#A B C D
#E F G H

# make blocks
# make function that randomly chooses blocks

import time
import pyglet
from pyglet.window import key
from pyglet import clock
from pyglet import graphics
from pyglet import image
from pyglet import sprite

MOVMENT_CONSTANT = 1
BOTTOM = -30

block = {'A':1} #this is Block
width = 460
height = 680
y = 0 #this is top of screen
x = 0 #this is center of screen
gameStart = False

def mainMenu():
    #title = image.load('title.png')
    play = image.load('play.png')
    quit = image.load('quit.png')
    
    mainMenuBatch = graphics.Batch()
    
    #titleSprite = sprite.Sprite(title, x=, y=, batch=mainMenuBatch)
    playButton = sprite.Sprite(play, x=100, y=350, batch=mainMenuBatch)
    quitButton = sprite.Sprite(quit, x=130, y=250, batch=mainMenuBatch)
    
    #if start game change startGame Variable
    
    mainMenuBatch.draw()
   
def fall(dt):
    global y
    
    if y > BOTTOM:
	y -= MOVMENT_CONSTANT
	print 'Y:', y

#create a window
window = pyglet.window.Window(width=width, height=height)

if gameStart:
    clock.schedule_interval(fall, 1)

@window.event
def on_draw():
    window.clear() 
    if gameStart:
        print 'startGame'
    else:
        mainMenu()

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