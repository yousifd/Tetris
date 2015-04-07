from constants import *
from mainmenu import *
from pausemenu import *
from board import *

from pyglet import app
from pyglet import clock
from pyglet.window import Window
from pyglet.window import key
from pyglet.window import mouse

# clock.set_fps_limit(60)
window = Window(width=WIDTH, height=HEIGHT)

# move this later inside the game method or class
gameStart = False
gameRunning = False

# move this later inside the game method or class
mainMenu = mainMenu()
pauseMenu = pauseMenu()

board = Board()

def quit():
    window.close()
    app.exit() 

@window.event
def on_draw():
    window.clear()
    if not gameStart:
        mainMenu.draw()
    elif board.gameStop:
        quit()
    elif not gameRunning:
        pauseMenu.draw()
    else:
        gameBatch.draw()
        
@window.event
def on_mouse_press(x, y, button, modifiers):
    global gameStart
    global gameRunning
    
    if button == mouse.LEFT:
        if not gameStart:
            if mainMenu.ifAbove('play', x, y):
                gameStart = True
                board.gameStop = False
                gameRunning = True
                clock.schedule_interval(board.fall, 1) 
                mainMenu.delete()
            elif mainMenu.ifAbove('quit', x, y):
                quit()
        if not gameRunning:
            if pauseMenu.ifAbove('resume', x, y):
                gameRunning = True
                clock.schedule_interval(board.fall, 1)
            if pauseMenu.ifAbove('quit', x, y):
                quit()
                  
@window.event
def on_key_press(symbol, modifiers):
    global gameRunning

    if symbol == key.LEFT and gameRunning:
        board.movePieceLeft()
    elif symbol == key.RIGHT and gameRunning:
        board.movePieceRight()
    elif (symbol == key.DOWN) and gameRunning:
        clock.unschedule(board.fall)
        clock.schedule_interval(board.fallFaster, 0.1)
    elif symbol == key.UP and gameRunning:
        board.rotatePiece(0)
        clock.schedule_interval(board.rotatePiece, 0.3)
    elif symbol == key.P and gameRunning:
        gameRunning = False
        clock.unschedule(board.fall)

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.DOWN and gameRunning:
        clock.unschedule(board.fallFaster)
        clock.schedule_interval(board.fall, 1)
    if symbol == key.UP and gameRunning:
        clock.unschedule(board.rotatePiece)

def game():
    app.run()