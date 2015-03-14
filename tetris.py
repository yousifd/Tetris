from constants import *
from mainmenu import *
from pieces import *

from pyglet import app
from pyglet import clock

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
        if not gameStart:
            if PLAY_BOUNDARYx <= x <= (PLAY_BOUNDARYx+PLAY_WIDTH) and PLAY_BOUNDARYy <= y <= (PLAY_BOUNDARYy+PLAY_HEIGHT):
                gameStart = True
                clock.schedule_interval(fall, 1) 
                mainMenu.delete()
            elif QUIT_BOUNDARYx <= x <= QUIT_BOUNDARYx+QUIT_WIDTH and QUIT_BOUNDARYy <= y <= QUIT_BOUNDARYy+QUIT_HEIGHT:
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