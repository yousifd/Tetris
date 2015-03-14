from menu import *

from pyglet.window import Window
from pyglet.window import key
from pyglet.window import mouse

#Move this later to a game method or class that passes window to the other mthods
window = Window(width=WIDTH, height=HEIGHT)

def mainMenu():
	mainMenu = Menu(window.width, window.height)

	# # mainMenu.addTitle('title.png', x, y)
	# mainMenu.addButton('play.png', PLAY_BOUNDARYx, PLAY_BOUNDARYy)
	# mainMenu.addButton('quit.png', QUIT_BOUNDARYx, QUIT_BOUNDARYy)

	mainMenu.addCenterButton('play.png', 15)
	mainMenu.addCenterButton('quit.png')

	return mainMenu