from constants import *
from mainmenu import *
from pieces import *

from pyglet import app
from pyglet import clock

#move this later inside the game method or class
gameStart = False

#move this later inside the game method or class
mainMenu = mainMenu()

def quit():
    window.close()
    app.exit() 

@window.event
def on_draw():
    window.clear() 
    if not gameStart:
        mainMenu.draw()
    gameBatch.draw()
        
@window.event
def on_mouse_press(x, y, button, modifiers):
    global gameStart
    
    if button == mouse.LEFT:
        print 'Left Button Clicked'
        if not gameStart:
            print 'Game not Started Yet'
            print mainMenu.ifAbove('play', x, y)
            print mainMenu.ifAbove('quit', x, y)
            if mainMenu.ifAbove('play', x, y):
                print 'Game Started'
                gameStart = True
                clock.schedule_interval(fall, 1) 
                mainMenu.delete()
            elif mainMenu.ifAbove('quit', x, y):
                print 'Game Quit'
                quit()
                  
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
	    app.exit()

def game():
    app.run()