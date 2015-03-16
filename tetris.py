from constants import *
from mainmenu import *
from board import *

from pyglet import app
from pyglet import clock

#move this later inside the game method or class
gameStart = False

#move this later inside the game method or class
mainMenu = mainMenu()

piece = T_shape(CENTER, TOP)

def quit():
    window.close()
    app.exit() 

@window.event
def on_draw():
    window.clear() 
    if not gameStart:
        mainMenu.draw()
    else:
        gameBatch.draw()
        
@window.event
def on_mouse_press(x, y, button, modifiers):
    global gameStart
    
    if button == mouse.LEFT:
        if not gameStart:
            if mainMenu.ifAbove('play', x, y):
                gameStart = True
                clock.schedule_interval(fall, 1, piece=piece) 
                mainMenu.delete()
            elif mainMenu.ifAbove('quit', x, y):
                quit()
                  
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        movePieceLeft(piece)
    elif symbol == key.RIGHT:
        movePieceRight(piece)
    elif symbol == key.DOWN:
        fall(0, piece)
    elif symbol == key.UP:
        rotatePiece(piece)
    elif symbol == key.ESCAPE:
	    window.close()
	    app.exit()

def game():
    app.run()