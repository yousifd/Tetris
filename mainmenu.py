from constants import *
from menu import *

from pyglet.window import Window
from pyglet.window import key
from pyglet.window import mouse

#Move this later to a game method or class that passes window to the other mthods
window = Window(width=WIDTH, height=HEIGHT)

def mainMenu():
	menu = Menu(window.width, window.height)

	# # menu.addTitle('title.png', x, y)

	menu.addCenterButton('play.png', 15)
	menu.addCenterButton('quit.png')

	return menu