from menu import *

import pyglet

#TODO<yousif>: Possibly Create Window class that has everything related to a window
window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

#change the 0, 0 when you figure out the positions issue
mainMenu = Menu(window.width, window.height)

# # mainMenu.addTitle('title.png', x, y)
# mainMenu.addButton('play.png', PLAY_BOUNDARYx, PLAY_BOUNDARYy)
# mainMenu.addButton('quit.png', QUIT_BOUNDARYx, QUIT_BOUNDARYy)

mainMenu.addCenterButton('play.png')
mainMenu.addCenterButton('quit.png')