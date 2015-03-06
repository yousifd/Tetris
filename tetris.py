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

gameStart = False

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
    global gameStart
    
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
    if symbol == key.LEFT:
        movePieceLeft()
    elif symbol == key.RIGHT:
        movePieceRight()
    elif symbol == key.DOWN:
        fall(0)
    elif symbol == key.UP:
        rotatePiece()
    elif symbol == key.ESCAPE:
	    window.close()
	    pyglet.app.exit()

pyglet.app.run()    

window.close()
pyglet.app.exit()
