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

mainMenuBatch = graphics.Batch()
gameBatch = graphics.Batch()

#title = image.load('title.png')
play = image.load('play.png')
quit = image.load('quit.png')
blockImage = image.load('block.png')

#titleSprite = sprite.Sprite(title, x=, y=, batch=mainMenuBatch)
playButton = sprite.Sprite(play, x=100, y=350, batch=mainMenuBatch)
quitButton = sprite.Sprite(quit, x=130, y=250, batch=mainMenuBatch)
blockSprite = sprite.Sprite(blockImage, x=WIDTH/2, y=HEIGHT, batch=gameBatch)

block = {'A':blockSprite} #this is Block
y = 648 #this is top of screen
x = WIDTH / 2 #this is center of screen
gameStart = False
   
def fall(dt):
    global y #FIX
    
    if y > BOTTOM:
	y -= MOVMENT_CONSTANT
	block['A'].set_position(x=x, y=y)
	print 'Y:', y

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
            if 100 <= x <= 363 and 350 <= y <= 423:
                gameStart = True
                clock.schedule_interval(fall, 1) 
                #titleSprite.delete()
                playButton.delete()
                quitButton.delete()
            elif 130 <= x <= 334 and 250 <= y <= 319:
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
