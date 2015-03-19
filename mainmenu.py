from constants import *
from menu import *

def mainMenu():
	menu = Menu(WIDTH, HEIGHT)

	# # menu.addTitle('title.png', x, y)

	menu.addCenterButton('play.png', 15)
	menu.addCenterButton('quit.png')

	return menu