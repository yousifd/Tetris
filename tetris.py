from constants import *
from mainmenu import *
from board import *

from pyglet import app
from pyglet import clock

#move this later inside the game method or class
gameStart = False

#move this later inside the game method or class
mainMenu = mainMenu()

board = Board()

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
                clock.schedule_interval(board.fall, 1) 
                mainMenu.delete()
            elif mainMenu.ifAbove('quit', x, y):
                quit()
                  
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        board.movePieceLeft()
    elif symbol == key.RIGHT:
        board.movePieceRight()
    elif symbol == key.DOWN:
        board.fall(0)
    elif symbol == key.UP:
        board.rotatePiece()
    elif symbol == key.ESCAPE:
	    window.close()
	    app.exit()

def game():
    app.run()