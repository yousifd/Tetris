#A B C D
#E F G H

# make blocks
# make function that randomly chooses blocks

import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import clock
from pyglet import graphics
from pyglet import image
from pyglet import sprite

WIDTH = 460
HEIGHT = 680
MOVMENT_CONSTANT = 1
BOTTOM = HEIGHT

block = {'A':1} #this is Block
y = 0 #this is top of screen
x = WIDTH / 2 #this is center of screen
gameStart = False

#title = image.load('title.png')
play = image.load('play.png')
quit = image.load('quit.png')

mainMenuBatch = graphics.Batch()

#titleSprite = sprite.Sprite(title, x=, y=, batch=mainMenuBatch)
playButton = sprite.Sprite(play, x=100, y=350, batch=mainMenuBatch)
quitButton = sprite.Sprite(quit, x=130, y=250, batch=mainMenuBatch)
   
def fall(dt):
    global y #FIX
    
    if y < BOTTOM:
	y += MOVMENT_CONSTANT
	print 'Y:', y

#create a window
window = pyglet.window.Window(width=WIDTH, height=HEIGHT)  

@window.event
def on_draw():
    window.clear() 
    if not gameStart:
        mainMenuBatch.draw()
        
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

pyglet.app.run()    

window.close()
pyglet.app.exit()
