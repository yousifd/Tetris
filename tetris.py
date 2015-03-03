#A B C D
#E F G H

# make blocks
# make function that randomly chooses blocks
# Size of play area 10x18 blocks 

from constants import *
from pieces import *

import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import clock
from pyglet import graphics
from pyglet import image
from pyglet import sprite

mainMenuBatch = graphics.Batch()

#title = image.load('title.png')
play = image.load('play.png')
quit = image.load('quit.png')

#titleSprite = sprite.Sprite(title, x=, y=, batch=mainMenuBatch)
playButton = sprite.Sprite(play, x=PLAY_BOUNDARYx, y=PLAY_BOUNDARYy, batch=mainMenuBatch)
quitButton = sprite.Sprite(quit, x=QUIT_BOUNDARYx, y=QUIT_BOUNDARYy, batch=mainMenuBatch)

y = HEIGHT #this is top of screen
x = WIDTH / 2 #this is center of screen
gameStart = False
   
def fall(dt):
    global y #FIX
    
    if y > BOTTOM:
	y -= MOVMENT_CONSTANT
	block['A'].set_position(x=x, y=y)
	print 'Y:', y
    else:
        y = HEIGHT

#create a window
window = pyglet.window.Window(width=WIDTH, height=HEIGHT)  

@window.event
def on_draw():
    window.clear() 
    if not gameStart:
        mainMenuBatch.draw()
    gameBatch.draw()
        
@window.event
def on_mouse_press(x, y, button, modifiers):
    global gameStart #FIX 
    
    if button == mouse.LEFT:
        if not gameStart:
            if PLAY_BOUNDARYx <= x <= (PLAY_BOUNDARYx+PLAY_WIDTH) and PLAY_BOUNDARYy <= y <= (PLAY_BOUNDARYy+PLAY_HEIGHT):
                gameStart = True
                clock.schedule_interval(fall, 1) 
                #titleSprite.delete()
                playButton.delete()
                quitButton.delete()
            elif QUIT_BOUNDARYx <= x <= QUIT_BOUNDARYx+QUIT_WIDTH and QUIT_BOUNDARYy <= y <= QUIT_BOUNDARYy+QUIT_HEIGHT:
                window.close()
                pyglet.app.exit()
                  
@window.event
def on_key_press(symbol, modifiers):
    global x #FIX(see bellow)

    if symbol == key.LEFT and x > 0:
        x -= MOVMENT_CONSTANT
        block['A'].set_position(x=x, y=y)
	print 'X:', x
    elif symbol == key.RIGHT and x < WIDTH - MOVMENT_CONSTANT:
	x += MOVMENT_CONSTANT
	block['A'].set_position(x=x, y=y)
	print 'X:', x
    elif symbol == key.DOWN:
        fall(0)
    elif symbol == key.UP:
        print 'Rotate'
    elif symbol == key.ESCAPE:
	window.close()
	pyglet.app.exit()

pyglet.app.run()    

window.close()
pyglet.app.exit()
