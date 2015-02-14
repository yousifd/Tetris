#A B C D
#E F G H

# make blocks
# make function that randomly chooses blocks
# Size of play area 10x18 blocks 

import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import clock
from pyglet import graphics
from pyglet import image
from pyglet import sprite

WIDTH = 360
HEIGHT = 648
MOVMENT_CONSTANT = 36
BOTTOM = 0

PLAY_WIDTH = 263
PLAY_HEIGHT = 73 
PLAY_BOUNDARYx = WIDTH/2 - 130
PLAY_BOUNDARYy = HEIGHT/2 

QUIT_WIDTH = 204
QUIT_HEIGHT = 69
QUIT_BOUNDARYx = WIDTH/2 - 100
QUIT_BOUNDARYy = HEIGHT/2 - 100

mainMenuBatch = graphics.Batch()
gameBatch = graphics.Batch()

#title = image.load('title.png')
play = image.load('play.png')
quit = image.load('quit.png')
blockImage = image.load('block.png')

#titleSprite = sprite.Sprite(title, x=, y=, batch=mainMenuBatch)
playButton = sprite.Sprite(play, x=PLAY_BOUNDARYx, y=PLAY_BOUNDARYy, batch=mainMenuBatch)
quitButton = sprite.Sprite(quit, x=QUIT_BOUNDARYx, y=QUIT_BOUNDARYy, batch=mainMenuBatch)
blockSprite = sprite.Sprite(blockImage, x=WIDTH/2, y=HEIGHT, batch=gameBatch)

block = {'A':blockSprite} #this is Block
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

    if symbol == key.LEFT:
        x -= MOVMENT_CONSTANT
        block['A'].set_position(x=x, y=y)
	print 'X:', x
    elif symbol == key.RIGHT:
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
