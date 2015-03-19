from constants import *
from menu import *

from pyglet.window import Window
from pyglet.window import key
from pyglet.window import mouse

def pauseMenu():
	menu = Menu(WIDTH, HEIGHT)

	# # menu.addTitle('pause.png', x, y)

	menu.addCenterButton('resume.png', 15)
	menu.addCenterButton('quit.png')

	return menu